import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 定义生成器（Generator）
class Generator(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(True),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(True),
            nn.Linear(hidden_size, output_size),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)

# 定义判别器（Discriminator）
class Discriminator(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(hidden_size, hidden_size),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(hidden_size, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

# 设置参数
input_size = 100  # 噪声向量的大小
hidden_size = 256
image_size = 28 * 28  # 生成28x28像素的图像
batch_size = 64

# 创建生成器和判别器
G = Generator(input_size, hidden_size, image_size)
D = Discriminator(image_size, hidden_size)

# 损失函数和优化器
criterion = nn.BCELoss()
d_optimizer = optim.Adam(D.parameters(), lr=0.0002)
g_optimizer = optim.Adam(G.parameters(), lr=0.0002)

# 定义生成图像的函数
def generate_images(generator, num_images):
    noise = torch.randn(num_images, input_size)
    generated_images = generator(noise).detach().view(num_images, 28, 28)
    return generated_images

# 训练GAN模型的简化版代码
num_epochs = 50

for epoch in range(num_epochs):
    # 训练判别器
    real_data = torch.randn(batch_size, image_size)  # 假设有真实数据
    fake_data = G(torch.randn(batch_size, input_size))
    
    d_real = D(real_data)
    d_fake = D(fake_data)
    
    d_loss_real = criterion(d_real, torch.ones(batch_size, 1))
    d_loss_fake = criterion(d_fake, torch.zeros(batch_size, 1))
    d_loss = d_loss_real + d_loss_fake
    
    D.zero_grad()
    d_loss.backward()
    d_optimizer.step()

    # 训练生成器
    noise = torch.randn(batch_size, input_size)
    fake_data = G(noise)
    g_loss = criterion(D(fake_data), torch.ones(batch_size, 1))
    
    G.zero_grad()
    g_loss.backward()
    g_optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch [{epoch}/{num_epochs}], d_loss: {d_loss.item()}, g_loss: {g_loss.item()}")

# 生成并显示图像
generated_images = generate_images(G, 16)
for i, img in enumerate(generated_images):
    plt.subplot(4, 4, i + 1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
plt.show()
