+++
kind  = "proof"
of    = "cor-zl-hasse-bound"
uses = ["cor-trf-point-counting", "prop-cohomological-finiteness", "prop-endpoints", "def-weil-frobenius-coefficient-twists", "thm-sc-proper-cohomology", "sk-def-sfb-pulled-back-coefficients", "sk-thm-sfb-proper-base-change", "sk-prop-scalar-six", "prop-weight-purity-roots"]
+++
Step 1: the point-count identity. The scheme $C_0$ is proper, so by
[cor-trf-point-counting] applied to the constant Weil sheaf,

$$
N_n:=\#C_0(\mathbf F_{q^n})
=\sum_{i\in\mathbf Z}(-1)^i\Tr\bigl(F^n\mid H^i(C,\Qlb)\bigr),
$$

where $F$ is the global geometric Frobenius in the
geometric-Frobenius convention.

Step 2: the range and the degree zero. By
[prop-cohomological-finiteness] (the constant sheaf on a scheme of
dimension $1$), $H^i(C,\Qlb)=0$ for $i\notin[0,2]$, and
$H^0(C,\Qlb)\cong\Qlb$ with geometric Frobenius acting as the
identity; hence $\Tr(F^n\mid H^0(C,\Qlb))=1$ for every $n$.

Step 3: the top degree. By [prop-endpoints] with $d=1$,
$H^2(C,\Qlb)\cong\Qlb(-1)$ Frobenius-equivariantly, and by
[def-weil-frobenius-coefficient-twists] geometric Frobenius acts on
$\Qlb(-1)$ by $q$; hence $\Tr(F^n\mid H^2(C,\Qlb))=q^n$.

Step 4: the dimension of $H^1$. By
[thm-sc-proper-cohomology] (the Kummer computation for a smooth
proper curve of genus $g$ over the algebraically closed field $k$),
for every $n'=\ell^r$, $r\geq1$, prime to $\operatorname{char}k$,

$$
H^1(C,\mathbf F_{n'})\cong(\mathbf Z/n'\mathbf Z)^{2g},
$$

and $H^q(C,\mathbf F_{n'})=0$ for $q>2$; these étale cohomology groups of
torsion sheaves are the pro-étale ones. The $\ell$-adic groups are obtained
from them as consequences of the condensed theory. Let
$a:C\to\operatorname{Spec}k$ be the structure morphism and
$M^q=H^q(C,\mathbf Z_\ell)=H^q(Ra_*\mathbf Z_{\ell,C})$, with
$\mathbf Z_{\ell,C}=p_C^*\mathbf Z_\ell$ ([sk-def-sfb-pulled-back-coefficients]).
Since $a$ is proper, $Ra_*\mathbf Z_{\ell,C}\in\Dbc(\operatorname{Spec}k,\mathbf Z_\ell)$
([sk-thm-sfb-proper-base-change]), so the $M^q$ are finitely generated
$\mathbf Z_\ell$-modules, almost all zero. The coefficient comparison for $Ra_*$
along $\mathbf Z_\ell\to\mathbf Z/\ell^r$ ([sk-prop-scalar-six]) gives
$Ra_*\mathbf Z_{\ell,C}\otimes^{\mathbf L}_{\mathbf Z_\ell}\mathbf Z/\ell^r\simeq R\Gamma(C,\mathbf Z/\ell^r)$,
hence short exact sequences

$$
0\to M^1/\ell^r\to H^1(C,\mathbf Z/\ell^r)\to M^2[\ell^r]\to0 .
$$

Writing $M^q\cong\mathbf Z_\ell^{\,b_q}\oplus T^q$ with $T^q$ finite, the
middle group has order $\ell^{2gr}$, while for $r$ large the outer groups
have orders $\ell^{rb_1}\,|T^1|$ and $|T^2|$. Comparing growth in $r$ gives
$b_1=2g$. Finally, the coefficient comparison along the flat map
$\mathbf Z_\ell\to\Qlb$ ([sk-prop-scalar-six]) gives
$H^1(C,\Qlb)\cong M^1\otimes_{\mathbf Z_\ell}\Qlb$, so

$$
\dim_{\Qlb}H^1(C,\Qlb)=2g.
$$

Step 5: the trace bound. By [prop-weight-purity-roots] with
$i=1$ and $d=1$, every eigenvalue $\alpha$ of $F$ on
$H^1(C,\Qlb)$ satisfies $|\iota(\alpha)|=q^{1/2}$. Let
$\alpha_1,\ldots,\alpha_{2g}$ be the eigenvalues with algebraic
multiplicity (Step 4). The trace equals the sum of the eigenvalues,
so, applying the field isomorphism $\iota$ and the triangle inequality
in $\mathbf C$,

$$
\left|\iota\bigl(\Tr(F^n\mid H^1(C,\Qlb))\bigr)\right|
\leq\sum_{j=1}^{2g}|\iota(\alpha_j)|^n=2g\,q^{n/2}.
$$

Step 6: assembly. Combining Steps 1, 2 and 3,

$$
N_n-1-q^n=-\Tr\bigl(F^n\mid H^1(C,\Qlb)\bigr)
\quad\text{in }\Qlb.
$$

The left-hand side is an integer, hence fixed by $\iota$, so by
Step 5,

$$
|N_n-(q^n+1)|=\left|\iota\bigl(\Tr(F^n\mid H^1(C,\Qlb))\bigr)\right|
\leq2g\,q^{n/2},
$$

which is the claimed bound.
