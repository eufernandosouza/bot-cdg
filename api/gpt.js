const openai = require("openai");
openai.apiKey = process.env.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;

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).send("Apenas POST permitido");
  }

  const { text } = req.body;

  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: text }],
      max_tokens: 200,
    });

    const resposta = response.choices[0].message.content;
    res.status(200).json({ text: resposta });
  } catch (error) {
    console.error("Erro:", error);
    res.status(500).json({ error: "Erro ao gerar resposta" });
  }
}
