+++
kind = "proof"
of = "det-thm-br-field-units"
+++
*Degree one.* $H^1(\operatorname{Spec}L_{\mathrm{ét}},\mathbf G_m)=0$ is
Hilbert 90 ([cor-sc-hilbert-90-field]).

*Degree two.* The field $L$ is $C_1$. Indeed, let $f$ be a homogeneous form
of degree $d$ in $N>d$ variables with coefficients in $L$. Its finitely many
coefficients generate a subextension $L_0\subseteq L$ of finite type over
$K$; being algebraic over $K$, it is a finite extension of $K$. The field
$K$ is $C_1$ by Tsen's theorem ([lem-sc-tsen]), hence so is $L_0$
([lem-sc-c1-finite-extension]), so $f$ has a nontrivial zero in
$L_0^N\subseteq L^N$. Therefore
$\operatorname{Br}(L)=H^2(\operatorname{Spec}L_{\mathrm{ét}},\mathbf G_m)=0$
by [lem-sc-c1-brauer-trivial].

*Degrees at least three.* Let $G=\operatorname{Gal}(L^{\mathrm{sep}}/L)$ and
$M=(L^{\mathrm{sep}})^\times$, a discrete $G$-module. Étale cohomology of
$\operatorname{Spec}L$ is the Galois cohomology $H^q(G,-)$ of the
corresponding discrete module (Stacks, Étale Cohomology, section on Galois
cohomology), so $H^q(\operatorname{Spec}L_{\mathrm{ét}},\mathbf G_m)=H^q(G,M)$.
For $q\geq1$ this group is torsion: it is the filtered colimit of the
cohomology groups of the finite quotients $G/U$ with coefficients in $M^U$,
and each of these is killed by $\#(G/U)$.

Fix a prime $\ell$ (possibly equal to $\operatorname{char}k$) and $q\geq3$.
Put $A=M[\ell]$, $B=\ell M$ and $Q=M/\ell M$; the modules $A$ and $Q$ are
killed by $\ell$, so they are torsion, and by [lem-sc-function-field-cd-one]

$$
H^i(G,A)=H^i(G,Q)=0\qquad(i\geq2).
$$

Consider the exact sequences

$$
0\to A\to M\xrightarrow{\ \ell\ }B\to0,\qquad
0\to B\hookrightarrow M\to Q\to0 .
$$

From the first, $H^q(G,A)=0$ gives that $H^q(G,M)\to H^q(G,B)$ is
injective. From the second, $H^{q-1}(G,Q)=0$ (as $q-1\geq2$) gives that
$H^q(G,B)\to H^q(G,M)$ is injective. The composite $M\to B\hookrightarrow M$
is multiplication by $\ell$, so multiplication by $\ell$ is injective on
$H^q(G,M)$. Thus the torsion group $H^q(G,M)$ has no $\ell$-torsion for any
prime $\ell$, hence vanishes.

*The last sentence.* A strict henselization $\mathcal O^{\mathrm{sh}}$ of a
local ring of $C$ is a filtered colimit of local rings of étale
$C$-schemes, and its fraction field is the corresponding colimit of their
function fields, each a finite separable extension of $K$; so it is
algebraic over $K$.
