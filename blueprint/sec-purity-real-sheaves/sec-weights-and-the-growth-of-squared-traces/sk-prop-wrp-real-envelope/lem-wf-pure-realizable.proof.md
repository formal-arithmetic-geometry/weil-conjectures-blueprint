+++
kind  = "proof"
of    = "lem-wf-pure-realizable"
+++
At a closed point $y$ of degree $m$, let $\alpha$ be a Frobenius
eigenvalue of $\mathcal F$. Purity of weight $w$ in
[def-weil-punctual-weights] gives
$|\iota(\alpha)|^2=q^{mw}=q_y^{w}$. The corresponding eigenvalue of
the second summand is $c^m\alpha^{-1}$ by
[def-wf-constant-weil-twist], and hence

$$
\iota\bigl(c^m\alpha^{-1}\bigr)
=\frac{q^{mw}}{\iota(\alpha)}
=\overline{\iota(\alpha)},
$$

because $q^{mw}=|\iota(\alpha)|^2=\iota(\alpha)\overline{\iota(\alpha)}$.
Since this holds for every eigenvalue and every degree, and is
involutionary, the local eigenvalue multiset of $\mathcal R(\mathcal F)$
is conjugation-stable at every closed point; by
[def-wf-iota-real] the sheaf $\mathcal R(\mathcal F)$ is
$\iota$-real. The
projection onto the first summand gives the realizability of
$\mathcal F$.
