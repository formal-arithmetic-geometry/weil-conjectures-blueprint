+++
kind  = "proof"
of    = "lemma-weil-pbc-curve-constructible-primary-reduction"
+++
The reduction map $r:C_{\mathrm{red}}\to C$ is a universal homeomorphism
([lemma-weil-pbc-universal-homeomorphism-site-equivalence]). Base change
along $r$ is an equivalence of small etale sites which preserves and reflects
covering families ([lemma-weil-pbc-universal-homeomorphism-coverings]); it
sends $F$ to $r^{-1}F$ and identifies all cohomology groups, the restriction
maps to opens, and, since $(C_{\mathrm{red}})_{k'}\to C_{k'}$ is again a
universal homeomorphism, the pullback maps to algebraically closed
extensions. Affineness, properness, constructibility and the torsion
conditions are unchanged. So $\mathcal C(C,F)$ follows from
$\mathcal C(C_{\mathrm{red}},r^{-1}F)$, and we may assume $C$ reduced.

*Constructible sheaves.* Let $F$ be a constructible torsion sheaf of
$\Lambda$-modules. A finite stratification with finite stalks gives one
exponent $N$ annihilating every stalk, hence $NF=0$. Write
$N=\prod_{\ell\mid N}\ell^{r_\ell}$. Bezout supplies integers $e_\ell$
which are $1$ modulo $\ell^{r_\ell}$ and $0$ modulo the other prime powers.
The mutually orthogonal endomorphisms $e_\ell:F\to F$ sum to the identity and
give the decomposition

$$
F\xrightarrow{\sim}\bigoplus_{\ell\mid N}F[\ell^{r_\ell}],
\qquad s\longmapsto(e_\ell s)_\ell,
$$

whose inverse is addition; the summands are constructible, and split short
exact sequences together with [lemma-weil-pbc-eight-curve-devissage] reduce
$\mathcal C(C,F)$ to the summands. If $\ell^rF=0$, use the exact
kernel–quotient sequence

$$
0\longrightarrow F[\ell]\xrightarrow{\iota}F
\xrightarrow{\pi}F/F[\ell]\longrightarrow0.
$$

Its outer terms are constructible, and the quotient is killed by
$\ell^{r-1}$ because $\ell^{r-1}s\in F[\ell]$. The sheaf $F[\ell]$ is a
constructible sheaf of $\mathbf F_\ell$-modules (its stalks are finite,
$\Lambda$ being finite), so it satisfies the eight assertions by hypothesis.
Induction on $r$ and [lemma-weil-pbc-eight-curve-devissage], which passes the
eight assertions from the outer terms of a short exact sequence to the middle
term, give $\mathcal C(C,F)$.

*Torsion sheaves.* The etale topos of the noetherian scheme $C$ is coherent.
Given finitely many local sections of $F$ on quasi-compact etale objects and
finitely many relations, their image generates a constructible subsheaf:
refine by a finite stratification on which the finitely generated stalk
groups are constant. Ordered by inclusion, these constructible subsheaves
$F_\lambda$ form a filtered system with $F=\varinjlim_\lambda F_\lambda$;
if $F$ is $p$-primary or of torsion prime to $\operatorname{char}k$, so is
every $F_\lambda$. By [lemma-weil-pbc-curve-filtered-cohomology], and
naturality of the restriction and pullback maps, every class of
$H^q(C,F)$, $H^q(U,F|_U)$ or $H^q(C_{k'},F|)$ comes from some stage and a
class dying in the colimit dies at a later stage. Hence the vanishing
assertions, the bijectivity of the pullback maps and the surjectivity of
$H^2(C,F)\to H^2(U,F|_U)$ pass from the $F_\lambda$ to $F$. The finiteness
assertions only concern constructible $F$, which is covered by the previous
step.
