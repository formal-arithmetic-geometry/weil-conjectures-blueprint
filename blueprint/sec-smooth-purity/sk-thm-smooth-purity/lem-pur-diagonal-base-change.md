+++
id = "lem-pur-diagonal-base-change"
kind = "lemma"
title = "Base change for the dualizing object of a projection"
order = 2009
uses = ["def-pur-co-smoothness", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-scheme-morphism-properties", "sbc-thm-etale-local-normal-form"]
+++
In the purity conventions of [def-pur-conventions],
let $f:X\to Y$ be smooth separated of pure relative dimension
$d$, put $W=X\times_YX$ with projections $p_1,p_2$. The square

$$
\begin{array}{ccc}
W& \xrightarrow{\ p_2\ }&X\\
p_1\big\downarrow &&\big\downarrow f\\
X&\xrightarrow{\ f\ }&Y
\end{array}
$$

is Cartesian and $p_1$ is smooth (the base change of $f$); by the
base-change compatibility of
[def-pur-co-smoothness],

$$
\omega_{p_1}=Rp_1^!\Lambda_X
\;\cong\;Lp_2^*Rf^!\Lambda_Y=Lp_2^*\omega_f,
$$

and symmetrically $\omega_{p_2}\cong Lp_1^*\omega_f$. In
particular, since $p_2\Delta=\operatorname{id}_X$,

$$
C(p_1,\Delta)=L\Delta^*\omega_{p_1}
\;\cong\;L\Delta^*Lp_2^*\omega_f
\;\cong\;\omega_f.
$$
