+++
id = "prose-D-01"
kind = "hidden"
title = "Cohomology of curves with torsion coefficients"
order = 907
+++
The proof of proper base change reduces to facts about the cohomology
of torsion sheaves on curves over an algebraically closed field:
vanishing above degree two, finiteness, and invariance under extension
of the algebraically closed base field
(Theorem [sk-thm-curve-package]). Over $\mathbf C$ these are statements
about a Riemann surface, which has the homotopy type of a CW complex of
dimension two, or of one if it is not compact. Algebraically one computes
instead. For a smooth proper connected curve $C$ of genus $g$ and $n$
invertible in $k$, the Kummer sequence $0\to\mu_n\to\mathbf G_m \xrightarrow{n}\mathbf G_m\to0$, the vanishing of $H^q(C,\mathbf G_m)$ for
$q\geq2$ (a consequence of Tsen's theorem) and the Jacobian of
Appendix [sec-picard-framework] give

$$
H^0(C,\mu_n)=\mu_n(k),\qquad H^1(C,\mu_n)=J(C)[n](k)\simeq(\mathbf Z/n)^{2g},
\qquad H^2(C,\mu_n)=\mathbf Z/n
$$

(Proposition [sk-thm-curveestimate]). For $\mathbf P^1$, which has $g=0$,
this fixes the normalization of the class of $\mathcal O(1)$ used in the
proof of proper base change (Remark [sk-rem-curve-twists]). Removing a
nonempty finite set of $r$ points kills $H^2$ and raises the rank of
$H^1$ to $2g+r-1$ (Proposition [sk-prop-curve-affine-kummer]).

Proper base change is needed for all torsion coefficients, so we treat
the characteristic prime as well, by the Artin–Schreier sequence
$0\to\mathbf F_p\to\mathbf G_a\xrightarrow{\varphi-1}\mathbf G_a\to0$.
It reduces the cohomology of $\mathbf F_p$ to the coherent cohomology of
$\mathcal O_C$, and shows that $H^q(C,\mathbf F_p)=0$ for $q\geq2$ on every
curve (Theorem [sk-thm-curve-package], $(C_3)$). Finiteness and invariance under field extension now
hold only for proper curves. On the affine line,
$H^1(\mathbf A^1_k,\mathbf F_p)=k[t]/\{h^p-h\}$ is infinite, and it grows
when $k$ is enlarged (Example [sk-rem-curve-wild-example]): the
Artin–Schreier torsors $y^p-y=at$, for $a\in k$, have pairwise distinct
classes, and over a larger field $k'$ there are new ones with
$a\in k'\setminus k$. This is why the corresponding assertions $(C_5)$ and
$(C_7)$ of Theorem [sk-thm-curve-package] require properness, and why
Lemma [sk-cor-curve-invariance] is stated for proper curves.

A general torsion sheaf is reduced to a constant one by two observations.
First, a sheaf supported on finitely many points has no cohomology in
positive degrees, so passing to the normalization of a curve, or
extending a sheaf by zero from a dense open subset, changes cohomology
only in degrees zero and one, and only by finite groups
(Lemmas [sk-lem-curve-normalization] and [sk-lem-curve-dense-open]).
Second, a finite $\mathbf F_\ell$-local system becomes a successive
extension of constant sheaves on a finite étale cover of degree $d$
prime to $\ell$, given by an $\ell$-Sylow subgroup of its monodromy, and
dividing the trace of the cover by $d$ shows that the local system is a
direct summand of the pushforward of its pullback
(Lemma [sk-lem-curve-sylow-trace]). The same device reappears in the
trace formula (Section [sec-trace-formula]). We follow the proof of
[Stacks, Tag 03SC](https://stacks.math.columbia.edu/tag/03SC). From the main text we use only the comparison of cohomology
(Theorem [sk-prop-sf-comparison]) and the stalks of finite direct
images (Lemma [sk-lem-pbc-finite]), both proved before proper base change.
The theorem implies Lemma [sk-cor-curve-invariance] by $(C_7)$.

Throughout this appendix, cohomology means cohomology on $C_{\mathrm{pro}\acute{e}t}$,
and the sheaves are *classical*: by
Theorem [sk-thm-pe-classical-sheaves] such a sheaf is the inverse image
$\nu_C^*G$ of a sheaf $G$ on $C_{\acute{e}t}$ along the comparison morphism.
By Theorem [sk-prop-sf-comparison], its cohomology, together with
the restriction and pullback maps, agrees with étale cohomology, so
we carry out all calculations on $C_{\acute{e}t}$ and transport them back by
$\nu_C^*$.
