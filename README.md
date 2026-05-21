# Тема: Иста задача, различен текст: робусност на LLM кон варијации на инструкција
Овој проект е изработен како Проектна задача по предметот **Обработка на природните јазици (NLP)**. Фокусот на истражувањето е како варијациите во текстуалните инструкции влијаат врз излезот на големите јазични модели (LLMs) и колку тие се конзистентни во својот стил и емотивен тон.

## Структура на проектот

```
onpj_final_project/
│
├── 1k_stories_100_genre.csv          # Датасет — 1000 раскази, 100 жанрови
│
├── few_shot_genre_classification.ipynb  # Few-shot со HuggingFace 
├── flant5_model.ipynb                   # FLAN-T5 класификација
├── gpt_model.ipynb                      # GPT-базиран пристап
├── mistral_model.ipynb                  # Mistral класификација
├── t5gemma_model.ipynb                  # T5/Gemma класификација
├── graphics.ipynb                        # Визуализации и споредба на резултати
│
└── README.md
```

---

## Датасет

| Атрибут | Вредност |
|---|---|
| Извор | [NLP 1K Stories Dataset – 100 Genres](https://github.com/FareedKhan-dev/NLP-1K-Stories-Dataset-Genres-100) |
| Вкупно раскази | 1 000 |
| Вкупно жанрови | 100 |
| Жанрови во фокус | 15 најзастапени |
| Формат | CSV (`title`, `story`, `genre`) |

### Топ 15 жанрови

`Historical Adventure` · `Science Fiction` · `Fantasy` · `Mystery` · `Thriller` · `Horror` · `Comedy` · `Crime` · `Dystopian` · `Cyberpunk` · `Post-Apocalyptic` · `Fairy Tale` · `Adventure` · `War` · `Superhero`

---

## Инсталација и употреба

### Барања

```bash
pip install transformers torch pandas matplotlib scikit-learn ipywidgets
```

### Покренување

```bash
git clone https://github.com/your-username/onpj_final_project.git
cd onpj_final_project
jupyter notebook
```

Потоа отвори го саканиот `.ipynb` фајл и изврши ги клетките по ред.

> **Напомена:** При прво покренување на `few_shot_genre_classification.ipynb`, моделот `facebook/bart-large-mnli` (~1.6 GB) ќе се симне автоматски.

---

## Резултати

Детална споредба на перформансите на моделите е достапна во `graphics.ipynb`.

