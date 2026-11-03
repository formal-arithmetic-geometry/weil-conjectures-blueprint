+++
kind  = "proof"
of    = "prop-trf-compact-support-perfectness"
+++
Let $C=R\Gamma_c(X,K)$, with compact support as in
[def-compact-support-direct-image-detailed], [def-trf-coefficient-conventions].
Here $A$ is an arbitrary finite commutative $\ell$-primary ring, say
annihilated by $\ell^N$, and $k=\Fbar$ is algebraically closed
([def-weil-finite-field-fiber]). No residue field of a distinguished
uniformizer is used. The argument runs in the order: proper finiteness and
cohomological dimension, then the constant projection formula, then finite Tor
amplitude, then perfectness. The final six-operation package is not used.

*Transport to the étale site.* The étale statements used below are applied
only after this transport. By [lem-sf-proetale-constructible-origin] there is
a bounded constructible complex $K'$ of $A$-modules on $X_{\Et}$ with
$K\cong\nu_X^*K'$, and by [lem-exc-comparison-tor-interval] $K'$ has the same
Tor amplitude $[a,b]$ as $K$ ([def-weil-finite-tor-amplitude]). Choose a
compactification $X\xrightarrow{j}\overline X\xrightarrow{\bar a}\Spec k$ as in
[def-compact-support-direct-image-detailed], so $C=R\Gamma(\overline X,j_!K)$,
and put $d=\dim\overline X$. The pullback $\nu^*$ commutes with $j_!$, with the
constant sheaves $M_X$ and with derived tensor products. By
[prop-weil-pbc-comparison-direct-image] it also commutes with $R\bar a_*$, and
sections over the point agree on the two sites
([def-weil-finite-coefficient-point]). Hence, for every finite $A$-module $M$,
$C\otimes^L_AM$ and $R\Gamma_c(X,K\otimes^L_AM_X)$ are computed by
$j_!K'$ and $j_!(K'\otimes^L_AM_X)$ on $\overline X_{\Et}$.

*Finite cohomology.* Forget the $A$-module structure to $\mathbf Z/\ell^N$.
Forgetting commutes with $j_!$ and with the derived direct image, and the
cohomology sheaves of $j_!K'$ stay constructible. The classical proper
finiteness theorem [obl-fin-comparison] then makes every $\mathrm H^i(C)$ a
finite group, hence a finite $A$-module. This is the general-finite-ring
clause of [prop-finite-compact-support-constructibility]. Only bounded
constructibility is used here. No claim is made that restriction of scalars
to $\mathbf Z/\ell^N$ preserves finite Tor amplitude.

*Finite Tor amplitude.* By [lem-sf-etale-direct-image-vanishing]
([Stacks, Tag 095U](https://stacks.math.columbia.edu/tag/095U)),
$R^q\bar a_*F=0$ for $q>2d$ and every sheaf of $A$-modules $F$ on
$\overline X_{\Et}$. The analogous pro-étale bound of
[def-weil-full-cohomological-dimension] is not used: by its warning it fails
for general pro-étale sheaves. For a finite $A$-module $M$, the étale
projection formula with a finitely presented constant coefficient
[lem-sf-projection-finite-constant], applied to $\bar a$, $j_!K'$ and $N=2d$,
together with $j_!K'\otimes^L_AM_{\overline X}\cong j_!(K'\otimes^L_AM_X)$, gives

$$
C\otimes_A^LM\xrightarrow{\sim}R\Gamma_c(X,K\otimes_A^LM_X)\in D^{[a,b+2d]}(A),
$$

because $K'\otimes^L_AM_X$ has cohomology sheaves in $[a,b]$. Every $A$-module
is the filtered union of its finite submodules. Derived tensor products and
cohomology commute with filtered colimits, so $C\otimes^L_AM\in D^{[a,b+2d]}(A)$
for every $A$-module $M$. Thus $C$ has Tor amplitude in $[a,b+2d]$. No
continuity theorem for $R\Gamma_c$ is needed.

*Perfectness.* Finite cohomology and finite Tor amplitude give perfectness
([Stacks, Tag 0658](https://stacks.math.columbia.edu/tag/0658)), as in
[lem-trf-finite-tor-amplitude-perfect]. So $C$ is represented by a bounded
complex of finite projective $A$-modules, which are finite free when $A$ is
local (e.g. $A=A_{E,n}$).

For $K_{\bar x}$, the exact inverse-image property
[prop-weil-pbc-inverse-image-exact] and the finite-stalk
condition of [def-weil-finite-torsion-constructibility] give
bounded finite cohomology. The tensor-vanishing definition
[def-weil-finite-tor-amplitude] is preserved by this inverse
image, so the same module-theoretic perfectness criterion applies.
Thus both objects lie in the perfect category used for categorical
trace in [def-trf-categorical-trace].
No preservation of finite Tor amplitude by a package summary is used
in this argument.

*Recorded in advance* from chapter *The trace formula* of the source.
