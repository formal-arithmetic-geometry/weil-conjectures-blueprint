+++
kind  = "proof"
of    = "cor-zl-hasse-bound"
uses = ["cor-trf-point-counting", "prop-cohomological-finiteness", "prop-endpoints", "def-weil-frobenius-coefficient-twists", "lem-sc-primitive-root", "def-sc-mu-trivialization", "def-sc-kummer-sequence", "lem-sc-kummer-les", "def-sc-pic0", "thm-sc-jacobian-representability", "def-wf-abelian-tate-module", "prop-av-tate-rank", "det-def-sfb-pulled-back-coefficients", "sk-prop-sfb-qlbar-colimit-x", "det-pe-continuous-cohomology-milnor", "sk-prop-scalar-six", "prop-weight-purity-roots"]
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

Step 4: the dimension of $H^1$. Since $k$ is algebraically closed and
$\ell\neq p$, there are primitive $\ell^r$-th roots of unity $\zeta_r\in k$
([lem-sc-primitive-root]), which we choose with $\zeta_{r+1}^{\ell}=\zeta_r$.
The trivializations $\theta_{\zeta_r}:\mathbf Z/\ell^r\xrightarrow{\sim}\mu_{\ell^r}$
of [def-sc-mu-trivialization] then carry the reductions
$\mathbf Z/\ell^{r+1}\to\mathbf Z/\ell^r$ to the $\ell$-th power maps
$\mu_{\ell^{r+1}}\to\mu_{\ell^r}$. The $\ell$-th power map of $\mathbf G_m$
and the identity of $\mathbf G_m$ form a morphism from the Kummer sequence for
$\ell^{r+1}$ to the one for $\ell^r$ ([def-sc-kummer-sequence]). By the
canonical identifications $H^1(C,\mu_{\ell^r})=\operatorname{Pic}(C)[\ell^r]$
of [lem-sc-kummer-les], valid as $C$ is proper, connected and reduced, the
$\ell$-th power maps therefore become multiplication by $\ell$. The degree
$\operatorname{Pic}(C)\to\mathbf Z$ is a homomorphism to a torsion-free group
([def-sc-pic0]), so
$\operatorname{Pic}(C)[\ell^r]=\operatorname{Pic}^0(C)[\ell^r]$, and
$\operatorname{Pic}^0(C)=J_C(k)$ for the Jacobian $J_C$, an abelian variety
of dimension $g$ ([thm-sc-jacobian-representability]). Hence

$$
\varprojlim_rH^1(C,\mathbf Z/\ell^r)\cong\varprojlim_rJ_C[\ell^r](k)
=T_\ell J_C\cong\mathbf Z_\ell^{2g}
$$

([def-wf-abelian-tate-module], [prop-av-tate-rank]). These étale cohomology
groups of torsion sheaves are the pro-étale ones. The $\ell$-adic groups are
obtained from them as consequences of the condensed theory. Let
$a:C\to\operatorname{Spec}k$ be the structure morphism and
$M^q=H^q(C,\mathbf Z_\ell)=H^q(Ra_*\mathbf Z_{\ell,C})$, with
$\mathbf Z_{\ell,C}=p_C^*\mathbf Z_\ell\cong\varprojlim_r(\mathbf Z/\ell^r)_C$
([det-def-sfb-pulled-back-coefficients], [sk-prop-sfb-qlbar-colimit-x]), a
limit of classical sheaves with epimorphic transition maps. The groups
$H^0(C,\mathbf Z/\ell^r)$ are finite, so the Milnor sequence of
[det-pe-continuous-cohomology-milnor] gives

$$
M^1\cong\varprojlim_rH^1(C,\mathbf Z/\ell^r)\cong\mathbf Z_\ell^{2g}.
$$

Finally, the coefficient comparison along the flat map
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
