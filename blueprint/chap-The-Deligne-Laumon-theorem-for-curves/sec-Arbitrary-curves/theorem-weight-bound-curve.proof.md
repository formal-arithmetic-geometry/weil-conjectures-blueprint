+++
kind = "proof"
of = "theorem-weight-bound-curve"
order = 1319
uses = ["lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "proposition-weights-j-boundary-points", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "theorem-weight-bound-affine-line", "lemma-finite-quasi-finite-direct-images"]
+++
On a geometrically connected curve we compare $j_*F$ with its
restriction to a dense affine open, where the affine case applies, and
we deduce the bounds from the localization sequence. The general case
reduces to this one, because a curve that is
not geometrically connected becomes a disjoint union of geometrically
connected ones after a finite constant extension.

Suppose first that $C_0$ is geometrically connected, and choose a dense affine open
$v:V_0\hookrightarrow U_0$. Since $F$ is lisse on $U_0$, the unit
$F\to v_*F|_V$ is an isomorphism by the last assertion of
Lemma [lemma-boundary-stalk]. Hence $j_*F$ is also the middle extension of
$F|_V$ from $V_0$ to $C_0$. On $V$, by Theorem [theorem-weight-bound-affine-curve] and
Lemma [lemma-extreme-degrees-affine-curve], $H_c^r(V,F)$ has weights at most $w+r$
for every $r$, and $H_c^0(V,F)=0$. On the complement, write $Z_0=C_0\setminus V_0$ and
$i$ for its inclusion; then the restriction of $j_*F$ to the finite set
$Z_0$ has weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], and its
cohomology is concentrated in degree zero. These two pieces are joined by the
localization sequence for $V\subset C$, which reads

$$
0=H_c^0(V,F)\to H_c^0(C,j_*F)\to H^0(Z,i^*j_*F)\to H_c^1(V,F)
\to H_c^1(C,j_*F)\to0,
$$

followed by an isomorphism $H_c^2(V,F)\simeq H_c^2(C,j_*F)$, and all
higher groups vanish. Over $\operatorname{Spec}k_0$ the bounds are
conditions on eigenvalues
(Lemmas [lemma-weil-sheaves-point-mixed]
and [lemma-bounding-weights-mixed-sheaf]), and we read them off
degree by degree. In degree zero, the group
$H_c^0(C,j_*F)$ injects into $H^0(Z,i^*j_*F)$, which has weights
at most $w$: Frobenius permutes the stalks at the geometric points over
each closed point of $Z_0$ cyclically, with the local Frobenius as the
power that returns to a stalk, as in the proof of
Theorem [theorem-weight-bound-affine-curve]. In degree one, $H_c^1(C,j_*F)$ is a quotient of $H_c^1(V,F)$,
which has weights at most $w+1$. In degree two the groups are
isomorphic, and the bound $w+2$ holds for $V$.

In general, the connected components of $C$ are defined over a finite
extension $k_m$ of $k_0$, and over $k_m$ each of them is a smooth
geometrically connected curve. For example, $\mathbf P^1_{\mathbf F_{q^2}}$,
viewed as a curve over $\mathbf F_q$, is connected, but $C$ has two
components, which Frobenius exchanges and which are defined over
$\mathbf F_{q^2}$. As Frobenius permutes the components, only its
$m$th power acts on the cohomology of each of them. On such a
component, $j_*F$ is the middle
extension of the restriction of $F$ to the dense open where the component
meets $U$, and this restriction is pure of weight $w$. Moreover, the group
$H^r_c(C,j_*F)$ is the direct sum of the groups of these components,
compatibly with the $m$th power of Frobenius. Hence the bound holds over
$k_m$ by the first case, and by
Lemma [lemma-weight-bound-constant-extension] it holds over $k_0$.
