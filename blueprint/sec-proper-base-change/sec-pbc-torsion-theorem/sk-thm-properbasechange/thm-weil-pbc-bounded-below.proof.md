+++
kind  = "proof"
of    = "thm-weil-pbc-bounded-below"
+++
*Step 1: sheaves killed by a prime.* Let $r$ be a prime and $E$ an abelian
sheaf on $X_{\Et}$ with $rE=0$, that is, a sheaf of $\mathbf F_r$-modules.
Restriction of scalars along $\mathbf Z\to\mathbf F_r$ is exact and
conservative, commutes with the inverse images $g^{-1},g'^{-1}$ and the direct
images $f_*,f'_*$, and also with $Rf_*,Rf'_*$, because an injective sheaf of
$\mathbf F_r$-modules has no higher direct images as an abelian sheaf. It
therefore carries the derived exchange morphism
[def-weil-pbc-derived-exchange] with $\mathbf F_r$-coefficients to the one
with $\mathbf Z$-coefficients. By [lemma-weil-pbc-prime-proper-base-change]
for $\Lambda=\mathbf F_r$, $\Ex_{\square,E}$ is an isomorphism, i.e. the
degreewise exchange maps $g^{-1}R^qf_*E\to R^qf'_*g'^{-1}E$ are isomorphisms
for all $q$.

*Step 2: torsion sheaves.* The proper morphism $f$ is quasi-compact and
quasi-separated, so by Step 1 and the prime-torsion dévissage
[lemma-weil-pbc-prime-torsion-devissage] the degreewise exchange maps are
isomorphisms at every torsion sheaf $F$ on $X_{\Et}$; equivalently
$\Ex_{\square,F}$ is an isomorphism in $\Dplus(Y'_{\Et})$.

*Step 3: bounded below complexes.* Let $K\in\Dplus(X_{\Et})$ have torsion
cohomology, with $\mathcal H^q(K)=0$ for $q<a$, and fix $n$. Both functors
$g^{-1}Rf_*$ and $Rf'_*g'^{-1}$ send objects with no cohomology below $m$ to
objects with no cohomology below $m$, so by the truncation criterion
[sbc-lem-bounded-below-truncation-criterion] and naturality of the exchange
morphism in $\tau_{\leq n}K\to K$, $\mathcal H^n(\Ex_{\square,K})$ is
identified with $\mathcal H^n(\Ex_{\square,\tau_{\leq n}K})$. The complex
$\tau_{\leq n}K$ is obtained from $\tau_{\leq a-1}K=0$ by the finitely many
truncation triangles
$\tau_{\leq q-1}K\to\tau_{\leq q}K\to\mathcal H^q(K)[-q]\to$, $a\leq q\leq n$
[lem-weil-pbc-truncation-triangle]. The exchange morphism is natural and
commutes with shifts, so it maps each of these triangles to a morphism of the
image triangles, and on the third terms it is the shift by $-q$ of
$\Ex_{\square,\mathcal H^q(K)}$, an isomorphism by Step 2 since
$\mathcal H^q(K)$ is torsion. Induction on $q$, using the long exact
cohomology sequences of the image triangles and the five lemma
[lem-weil-pbc-five-lemma], shows that $\Ex_{\square,\tau_{\leq q}K}$ is an
isomorphism for all $q\leq n$. Hence $\mathcal H^n(\Ex_{\square,K})$ is an
isomorphism for every $n$, and $\Ex_{\square,K}$ is an isomorphism in
$\Dplus(Y'_{\Et})$.
