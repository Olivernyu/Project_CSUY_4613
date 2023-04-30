import streamlit as st
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Function to load the pre-trained model

def load_finetune_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    sentiment_pipeline = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)
    return sentiment_pipeline

# Streamlit app
st.title("Multi-label Toxicity Detection App")
st.write("Enter a text and select the fine-tuned model to get the toxicity analysis.")

# Input text
default_text = "You might be the most stupid person in the world."
text = st.text_input("Enter your text:", value=default_text)

category = {'LABEL_0': 'toxic', 'LABEL_1': 'severe_toxic', 'LABEL_2': 'obscene', 'LABEL_3': 'threat', 'LABEL_4': 'insult', 'LABEL_5': 'identity_hate'}


# Model selection
model_options = {
    "Olivernyu/finetuned_bert_base_uncased": {
        "description": "This model detects different types of toxicity like threats, obscenity, insults, and identity-based hate in text. The table is prepopulated with some data, the table will be displayed once you hit analyze.",
    },
    "distilbert-base-uncased-finetuned-sst-2-english": {
        "labels": ["NEGATIVE", "POSITIVE"],
        "description": "This model classifies text into positive or negative sentiment. It is based on DistilBERT and fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.",
    },
    "textattack/bert-base-uncased-SST-2": {
        "labels": ["LABEL_0", "LABEL_1"],
        "description": "This model classifies text into positive(LABEL_1) or negative(LABEL_0) sentiment. It is based on BERT and fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.",
    },
    "cardiffnlp/twitter-roberta-base-sentiment": {
        "labels": ["LABEL_0", "LABEL_1", "LABEL_2"],
        "description": "This model classifies tweets into negative (LABEL_0), neutral(LABEL_1), or positive(LABEL_2) sentiment. It is based on RoBERTa and fine-tuned on a large dataset of tweets.",
    },
}
selected_model = st.selectbox("Choose a fine-tuned model:", model_options)

st.write("### Model Information")
st.write(f"**Description:** {model_options[selected_model]['description']}")

initial_table_df = pd.DataFrame(columns=["Text (portion)", "Toxicity class 1", "Class 1 probability", "Toxicity class 2", "Class 2 probability"])
initial_table_data = [{'Text (portion)': ["who's speaking? \n you goddamn cocksucker you know "],
  'Toxicity class 1': ['obscene'],
  'Class 1 probability': 0.7282997369766235,
  'Toxicity class 2': ['toxic'],
  'Class 2 probability': 0.2139672487974167},
 {'Text (portion)': ['::Here is another source: Melissa Sue Halverson (2'],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.24484945833683014,
  'Toxicity class 2': ['obscene'],
  'Class 2 probability': 0.1627064049243927},
 {'Text (portion)': [', 8 November 2007 (UTC) \n\n All I can say is, havin'],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.7277262806892395,
  'Toxicity class 2': ['obscene'],
  'Class 2 probability': 0.2502792477607727},
 {'Text (portion)': ['::::I only see that at birth two persons are given'],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.2711867094039917,
  'Toxicity class 2': ['insult'],
  'Class 2 probability': 0.15477754175662994},
 {'Text (portion)': ["* There you have it: one man's Barnstar is another"],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.5408656001091003,
  'Toxicity class 2': ['insult'],
  'Class 2 probability': 0.12563346326351166},
 {'Text (portion)': ['" \n\n == Fact == \n\n Could just be abit of trivial f'],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.35239243507385254,
  'Toxicity class 2': ['obscene'],
  'Class 2 probability': 0.1686778962612152},
 {'Text (portion)': ['HE IS A GHAY ASS FUCKER@@!!'],
  'Toxicity class 1': ['obscene'],
  'Class 1 probability': 0.7819343209266663,
  'Toxicity class 2': ['toxic'],
  'Class 2 probability': 0.16951803863048553},
 {'Text (portion)': ["I'VE SEEN YOUR CRIMES AGAINST CHILDREN AND I'M ASH"],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.8491994738578796,
  'Toxicity class 2': ['threat'],
  'Class 2 probability': 0.04749392718076706},
 {'Text (portion)': [':While with a lot of that essay says, general time'],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.282654732465744,
  'Toxicity class 2': ['obscene'],
  'Class 2 probability': 0.15901680290699005},
 {'Text (portion)': ['== Help == \n\n Please members of wiki, help me. My '],
  'Toxicity class 1': ['toxic'],
  'Class 1 probability': 0.3118911385536194,
  'Toxicity class 2': ['obscene'],
  'Class 2 probability': 0.16506287455558777}]
for d in initial_table_data:
    initial_table_df = pd.concat([initial_table_df, pd.DataFrame(d)], ignore_index=True)
# Load the model and perform toxicity analysis

if "table" not in st.session_state:
    st.session_state['table'] = initial_table_df

if st.button("Analyze"):
    if not text:
        st.write("Please enter a text.")
    else:
        with st.spinner("Analyzing toxicity..."):
            if selected_model == "Olivernyu/finetuned_bert_base_uncased":
                toxicity_detector = load_model(selected_model)
                outputs = toxicity_detector(text, top_k=2)
                category_names = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
                results = []
                for item in outputs:
                    results.append((category[item['label']], item['score']))

                # Create a table with the input text (or a portion of it), the highest toxicity class, and its probability
                table_data = {
                    "Text (portion)": [text[:50]],
                    "Toxicity class 1": [results[0][0]],
                    f"Class 1 probability": results[0][1],
                    "Toxicity class 2": [results[1][0]],
                    f"Class 2 probability": results[1][1]
                }

                # Concatenate the new data frame with the existing data frame
                st.session_state['table'] = pd.concat([pd.DataFrame(table_data), st.session_state['table']], ignore_index=True)

                # Update the table with the new data frame
                st.table(st.session_state['table'])
            else:
                st.empty()
                sentiment_pipeline = load_model(selected_model)
                result = sentiment_pipeline(text)
                st.write(f"Sentiment: {result[0]['label']} (confidence: {result[0]['score']:.2f})")
                if result[0]['label'] in ['POSITIVE', 'LABEL_1'] and result[0]['score']> 0.9:
                    st.balloons()
                elif result[0]['label'] in ['NEGATIVE', 'LABEL_0'] and result[0]['score']> 0.9:
                    st.error("Hater detected.")
else:
    st.write("Enter a text and click 'Analyze' to perform toxicity analysis.")
