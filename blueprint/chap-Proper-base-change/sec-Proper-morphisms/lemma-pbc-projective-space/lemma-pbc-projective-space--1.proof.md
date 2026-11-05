+++
kind = "proof"
of = "lemma-pbc-projective-space--1"
order = 395002
uses = ["lemma-finite-morphisms", "lemma-composition-cancellation"]
+++
We argue by induction on $n$. For $n=0$, the identity of $S$ is finite,
so Lemma [lemma-finite-morphisms] gives $\mathrm{PBC}_\Lambda(p_0)$.
For the induction step, the hypothesis applied to $X_n$ gives
$\mathrm{PBC}_\Lambda(X_{n+1}\to X_n)$, and the induction hypothesis gives
$\mathrm{PBC}_\Lambda(p_n)$. Lemma [lemma-composition-cancellation](i)
therefore gives $\mathrm{PBC}_\Lambda(p_{n+1})$.
