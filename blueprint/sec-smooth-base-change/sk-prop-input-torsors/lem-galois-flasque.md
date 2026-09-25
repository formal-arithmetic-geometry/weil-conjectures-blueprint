+++
id = "lem-galois-flasque"
kind = "lemma"
title = "Flasque resolutions and the connecting map"
order = 1407
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves"]
+++
Let $\mathcal F$ be a sheaf of abelian groups on $Y_{\Et}$. Then there
is an exact sequence of sheaves

$$
0\longrightarrow\mathcal F\longrightarrow I\xrightarrow{\ d\ }J
\longrightarrow0
$$

with $I$ and $J$ flasque and $H^q(Y_{\Et},I)=H^q(Y_{\Et},J)=0$ for
$q\ge1$; consequently the connecting map induces

$$
H^1(Y_{\Et},\mathcal F)\cong\operatorname{coker}\bigl(d_Y:I(Y)\to
J(Y)\bigr).
$$

## Proof

Take the Godement construction, for sheaves on $Y_{\Et}$ in the sense
of [def-weil-pbc-etale-sheaves] and with the cohomology of
[def-weil-pbc-etale-cohomology]:
$G(\mathcal G)(U)=\prod_{u\in U}\mathcal G_u$ is a sheaf containing $\mathcal G$ and is flasque, restriction
maps being surjective because they only discard coordinates; iterating
gives a flasque resolution. A flasque sheaf has vanishing higher
cohomology: for $0\to\mathcal A\to\mathcal B\to\mathcal C\to0$ with
$\mathcal A$ flasque, sections of $\mathcal B$ over an open surject
onto those of $\mathcal C$ (local liftings are patched using the
flasqueness of $\mathcal A$), so global sections are right exact on such
sequences and dimension shifting gives $H^q(\mathcal A)=0$ for $q\ge1$.
Truncating the resolution in degrees $\le1$ gives the displayed sequence
with $H^q(I)=H^q(J)=0$; the long exact sequence identifies
$H^1(Y_{\Et},\mathcal F)$ with $\operatorname{coker}(d_Y)$ and
$H^0$ with $\ker d_Y$.
