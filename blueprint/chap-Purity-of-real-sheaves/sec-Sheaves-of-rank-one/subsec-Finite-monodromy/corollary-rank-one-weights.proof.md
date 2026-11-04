+++
kind = "proof"
of = "corollary-rank-one-weights"
order = 1102
uses = ["theorem-rank-one-sheaves-have-finite"]
+++
We separate from $\chi$ the part that depends only on the degree. Put
$\varepsilon(w)=\chi(w)c^{-\deg w}$, a character of $W(U_0)$ that is
trivial on $s$.  Every element of $W(U_0)$ can be written as $w=gs^d$
with $g\in\pi_1(U)$ and $d=\deg w$, and then
$\varepsilon(w)=\chi(g)\chi(s)^dc^{-d}=\chi(g)$. So $\varepsilon$
has the same image as $\chi|_{\pi_1(U)}$, which is finite
by Theorem [theorem-rank-one-sheaves-have-finite].  At a closed point $x$ the
eigenvalue is $\varepsilon(\operatorname{Frob}_x)c^{\deg(x)}$. The first factor
has finite order, hence complex absolute value one. Therefore the eigenvalue
has absolute value $q_x^{\lambda_\iota(c)/2}$.  This number does not depend
on $s$, because changing $s$ multiplies $c$ by a value of $\chi$ on
$\pi_1(U)$, which has finite order.
