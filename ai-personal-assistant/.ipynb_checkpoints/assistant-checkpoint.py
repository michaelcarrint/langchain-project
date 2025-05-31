{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d78f4eb7-12b1-4c6e-910d-bed1b825555b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/qy/pvhxy8l11w110x4vspdjj_v40000gn/T/ipykernel_77578/2571259463.py:13: LangChainDeprecationWarning: Please see the migration guide at: https://python.langchain.com/docs/versions/migrating_memory/\n",
      "  memory = ConversationBufferMemory()\n",
      "/var/folders/qy/pvhxy8l11w110x4vspdjj_v40000gn/T/ipykernel_77578/2571259463.py:14: LangChainDeprecationWarning: The class `ConversationChain` was deprecated in LangChain 0.2.7 and will be removed in 1.0. Use :meth:`~RunnableWithMessageHistory: https://python.langchain.com/v0.2/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html` instead.\n",
      "  conversation = ConversationChain(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "👋 Hi there, I am your personal Assistant, Enter 'exit', to stop\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import openai\n",
    "from dotenv import load_dotenv, find_dotenv\n",
    "_ = load_dotenv(find_dotenv()) # read local .env file\n",
    "openai.api_key = os.environ['OPENAI_API_KEY']\n",
    "\n",
    "# LangChain Components\n",
    "from langchain_openai import ChatOpenAI\n",
    "from langchain.chains import ConversationChain\n",
    "from langchain.memory import ConversationBufferMemory\n",
    "\n",
    "llm = ChatOpenAI(model=\"gpt-4o-mini\", temperature=0.0)\n",
    "memory = ConversationBufferMemory()\n",
    "conversation = ConversationChain(\n",
    "    llm = llm,\n",
    "    memory = memory,\n",
    "    verbose = True\n",
    ")\n",
    "print(\"👋 Hi there, I am your personal Assistant, Enter 'exit', to stop\\n\")\n",
    "\n",
    "\n",
    "while True:\n",
    "    user_input = input(\"> \")\n",
    "    if user_input.lower() in [\"exit\", \"quit\"]:\n",
    "        print(\"Goodbye✌️\")\n",
    "        break\n",
    "response = conversation.predict(input=user_input)\n",
    "print(\"🤖Personal Assistant\\n\\n\", response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a47fc1c-2aec-48ca-9a26-272fff39b0ba",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
