+++
id = "sk-thm-nagata-sketch-two-open"
kind = "section"
title = "Two-open compactification"
order = 284
uses = ["sk-lem-nagata-sketch-common", "sk-lem-nagata-sketch-dense-valuative", "sk-prop-nagata-sketch-key-disjointness"]
lean = ["AlgebraicGeometry.HasCompactification.of_two_open_cover"]
+++
*Theorem (sketch).*

Let $S$ be a Noetherian scheme and let $U\to S$ be a separated
morphism which is locally of finite type and quasi-compact. Let
$U_1,U_2\subseteq U$ be open subschemes with $U_1\cup U_2=U$ and
$U_1\cap U_2$ dense in $U$, such that both composites $U_i\hookrightarrow U\to S$
are compactifiable.
Then $U\to S$ is compactifiable.

## Proof

Put $D=U_1\cap U_2$. Choose compactifications of the $U_i\to S$ and turn
them into prepared sides $U_i\subseteq V_i\subseteq X_i$ with
$\psi_i\colon V_i\to U$ and forbidden boundaries $B_{i,j}$, improved as
in [sk-prop-nagata-sketch-key-disjointness] so that
$X_{12}\cap(B_{1,2}\times_SB_{2,1})=\varnothing$.
For $\{i,j\}=\{1,2\}$ form

$$
X_i^\circ=X_i\setminus B_{i,j},\qquad
W_i=U\amalg_{U_i}X_i^\circ.
$$

These are separated finite-type $S$-schemes. Indeed the graph
$V_i\to U\times_SX_i$ is a proper immersion, hence closed.
Its restriction to $U\times_SX_i^\circ$ is exactly the overlap
$U_i$: all points over $U\setminus U_i=Z_j$ have been removed.
The closed-overlap criterion therefore gives separatedness of $W_i$.

Apply [sk-lem-nagata-sketch-common] to the common open $U$ in the
two $W_i$. It gives proper $U$-admissible blow-ups $W_i'\to W_i$
and a separated finite-type scheme $W$ covered by the $W_i'$.
The copy of $U$ is scheme-theoretically dense in each $W_i$ and $W_i'$:
this follows from density of $U_i$ in $X_i$ and preservation of density
under admissible blow-ups. Since $D$ is topologically dense in $U$,
it is dense in $W$. It is a quasi-compact open, since all these schemes
are Noetherian.

Let $A$ be a valuation ring with fraction field $K$, and consider a
generic map $\Spec K\to D$ over $\Spec A\to S$.
Properness extends it to $g_i:\Spec A\to X_i$ for both $i$.
The pair $(g_1,g_2)$ factors through the closed subscheme $X_{12}$:
it does so generically, and $A\hookrightarrow K$ is injective.
By [sk-prop-nagata-sketch-key-disjointness], the two closed-point
images cannot both meet the forbidden boundaries $B_{1,2},B_{2,1}$.
Hence one $g_i$ lands in $X_i^\circ$, since an open of a local spectrum
containing its closed point is the whole spectrum.
It gives a map to $W_i$, which lifts to $W_i'$ by properness of the
blow-up and then maps to $W$. Separatedness makes the extension unique.
By [sk-lem-nagata-sketch-dense-valuative], $W\to S$ is proper.
The resulting quasi-compact open immersion $U\hookrightarrow W$
is the desired compactification.
