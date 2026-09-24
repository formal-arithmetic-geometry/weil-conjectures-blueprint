+++
id = "lemma-weil-pbc-epsilon-unit-counit-naturality"
kind = "lemma"
title = "Naturality of the comparison unit and counit"
order = 1905
uses = ["def-weil-pbc-epsilon-comparison", "def-weil-pbc-epsilon-unit-counit"]
+++
For $\alpha:F\to F'$ on $X_{\mathrm{et}}$ and $\beta:G\to G'$ on
$X_{\mathrm{proet}}$, one has

$$
\begin{aligned}
(\epsilon_{X,*}\epsilon_X^{-1}\alpha)\eta^X_F
&=\eta^X_{F'}\alpha,\\
\beta\varepsilon^X_G
&=\varepsilon^X_{G'}(\epsilon_X^{-1}\epsilon_{X,*}\beta).
\end{aligned}
$$

## Proof

At an etale object $U$, both sides of the first equation send $s\in F(U)$
to the class $(1_{\iota_XU},\alpha_U(s))$. At a pro-etale object $W$, apply
the second equation to a representative $(W\xrightarrow{a}\iota_XU,s)$.
Both sides give
$\beta_W(G(a)(s))=G'(a)(\beta_{\iota_XU}(s))$ by naturality of $\beta$.
These equations survive sheafification and prove the asserted naturality.
