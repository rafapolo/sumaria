An experiment using Co-Pilot and Python to prompt and summarize youtube videos using [open LLM models](https://ollama.com/search) .

# SumarIA

Sumaria is designed to fetch transcripts from YouTube videos and generate concise summaries using a local LLM model. It consists of three main components: the application entry point, the youtube transcript fetcher and the summarizer getting the transcription main themes and key points.

## Project Structure

```
sumaria
├── src
│   ├── sumaria.py            # Entry point of the application
│   ├── summarizer.py         # Class prompting main themes and summaries
│   ├── transcript_fetcher.py # Class for fetching youtube transcripts
├── cached                    # Storing cached transcripts and summaries
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Usage & Example

Use Sumaria replacing `<video_id>` with the ID of the YouTube video you want to summarize:

Summarizing [NVIDIA CEO Jensen Huang's Vision for the Future
](https://www.youtube.com/watch?v=7ARBJQn6QkM) 1-hour long interview:

```
$ python src/sumaria.py 7ARBJQn6QkM

= Sumaria =
Fetching transcript for video 7ARBJQn6QkM
languages: en

Generating summary...
- AI and Technology
- Impact of AI on Various Fields
- Responsibility in Technology Development
- Influence of Gaming Industry

saved at ./cached/7ARBJQn6QkM/summary.md
in 50.18 seconds
```

Took ~1 minute on a Mac M4 Apple M4 10-core GPU to be generated.

See original [transcript](cached/7ARBJQn6QkM/transcript.txt) and resulting [summary](cached/7ARBJQn6QkM/summary.md).

## Installation

1. Clone the repository:

2. Install the required dependencies:
- `requests`
- `youtube-transcript-api`
```
$ pip install -r requirements.txt
```


3. Use local [llama](https://ollama.com/) models
```
$ ollama pull mistral:instruct
$ ollama serve # at http://localhost:11434 
```

## Notes

**Human:**

Since the model is limited to an amount of tokens ingestion, the summary has to be broken in chunks, breaking a more integral view of what the transcription is about. A summary of the summary might be needed, since the current design asks for 4 key-points per chunk of 2000 chars. The results are still long as a 28 chunks transcript generates extensive 112 key points. The chunks should also be better broken on spaces or dots, avoiding broken words per chunk. Anyhow, test other models and better understanding the semantical chunks as a pre or post prompt is a work-to-be-done to have consice information. The correct prompting technique becames the relevant Engineering for the ideal summary.


**Modelo Largo de Linguagem em Brasileiro Poético:**

Sobre Fragmentos, Sentido e a Busca por Clareza

Limitados pelos tokens do modelo, somos levados a fragmentar o todo — quebrando o fluxo contínuo da fala em blocos digeríveis. Trocamos continuidade por viabilidade, esculpindo uma transcrição extensa em pedaços de 2 mil caracteres. Cada fragmento é instruído a responder seus quatro pontos-chave, mas ao multiplicar isso por dezenas de partes, não se sintetiza holísticamente — acumulam-se fragmentos.

Sonhamos com um resumo que soe como música: íntegro, fluido, intuitivo. Que a atenção do modelo seja conduzida não apenas à superfície, mas ao sentido original, à narrativa, à verdade da compreensão. Para chegar lá, é preciso nos desfragmentar. Que nenhuma frase seja cortada no meio do pensamento, que nenhuma palavra seja partida ao meio - ou que se rasgue em loop como representação da representação?

Aqui delineamos os limites da síntese rasa — até que ela aprenda a respeitar a voz de quem fala.
