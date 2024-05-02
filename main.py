import tkinter as tk
from PIL import Image, ImageTk


class PecasComputador:
    def __init__(self, root):
        self.root = root
        self.root.title("Conhecendo mais sobre os computadores...")

        self.label_titulo = tk.Label(root, text="Aprenda mais sobre peças")
        self.label_titulo.pack(pady=5)

        self.label_informacao = tk.Label(root, text="Selecione a peça desejada")
        self.label_informacao.pack(pady=5)

        self.parts = {
            "PLACA MÃE": {
                "Informação": "É a unidade central de um sistema de computador, conectando todos os componentes de hardware e permitindo que eles se comuniquem entre si.",
                "image": "mobo.jpg"},
            "CPU": "É o cérebro do computador, responsável por processar todas as informações e executar as tarefas.",
            "RAM": "É a memória de acesso aleatório do computador, usada para armazenar temporariamente dados e instruções enquanto o computador está em uso.",
            "GPU": "É a unidade de processamento gráfico do computador, responsável por renderizar gráficos e imagens em uma tela.",
            "SSD": " É um tipo de armazenamento de dados que usa memória flash para armazenar informações, oferecendo tempos de leitura e gravação mais rápidos do que os discos rígidos tradicionais.",
            "HD": " É um tipo de armazenamento de dados que usa discos magnéticos para armazenar informações, oferecendo capacidades de armazenamento maiores do que os SSDs, mas com tempos de leitura e gravação mais lentos.",
            "FONTE DE ALIMENTAÇÃO": " É o componente responsável por fornecer energia elétrica a todos os componentes do computador, garantindo que o sistema funcione corretamente.",

        }

        self.parte_selecionada = tk.StringVar()
        self.parte_selecionada.set("Selecione uma peça")

        self.opcoes = tk.OptionMenu(root, self.parte_selecionada, *self.parts.keys(), command=self.display)
        self.opcoes.pack()

        self.parte_informacao = tk.Label(root, text="")
        self.parte_informacao.pack(pady=5)

        self.parte_imagem = tk.Label(root, text="")
        self.parte_imagem.pack(pady=5)

    def display(self, partes):
        informacoes = self.parts.get(partes, "Peça não encontrada")
        self.parte_informacao.config(text=informacoes)

        image_path = self.parts.get(partes, {}).get("image")
        if image_path:
            image = Image.open(image_path)
            image = image.resize((200, 200))
            foto =  ImageTk.PhotoImage(image)
            self.parte_imagem.config(image=foto)
            self.parte_imagem.image = foto



def main():
    root = tk.Tk()
    app = PecasComputador(root)
    root.mainloop()


if __name__ == "__main__":
    main()
