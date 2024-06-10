import os

pasta = "lista9"
os.makedirs(pasta, exist_ok=True)

for i in range(1, 21):
    with open(os.path.join(pasta, f"ex{i}.py"), 'w') as f:
        f.write("# Este é o arquivo ex{}.py\n".format(i))

print("Arquivos criados com sucesso!")
