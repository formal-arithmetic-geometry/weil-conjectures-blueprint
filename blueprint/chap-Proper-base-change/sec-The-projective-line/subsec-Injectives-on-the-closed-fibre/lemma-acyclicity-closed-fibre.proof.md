+++
kind = "proof"
of = "lemma-acyclicity-closed-fibre"
order = 373
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-torsion-sheaves", "theorem-gabber-affine-proper-base-change", "theorem-finite-etale-covers-proper-henselian", "lemma-finite-morphisms", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
We prove vanishing on affine charts by Gabber's theorem, deduce the case
$q\geq2$ by Mayer–Vietoris, and treat $q=1$ by lifting classes to finite
torsors over $\mathbf P^1_R$, where injectivity of $I$ kills them.

*Step 1: affine opens.* Let $W=\operatorname{Spec}B$ be an affine open of
$\mathbf P^1_R$ and set $J=\mathfrak mB$. We show that $I_0|_{W_0}$ has no
cohomology in positive degrees. Since the pair $(B,J)$ need not be henselian, we pass
to its henselization $(B^h,JB^h)$, for which $B^h/JB^h=B/J$. Moreover, $B^h$ is the
filtered colimit of the étale $B$-algebras $B'$ equipped with
$B'/JB'\simeq B/J$. Gabber's theorem (Theorem [theorem-gabber-affine-proper-base-change]) and continuity of étale
cohomology give

$$
H^q(W_0,I_0|_{W_0})
\simeq H^q(\operatorname{Spec}B^h,I|)
\simeq\varinjlim_{B'}H^q(\operatorname{Spec}B',I|).
\tag{4.11}
$$

Every group on the right vanishes for $q>0$, because the restriction of an
injective sheaf to an étale object is injective: the restriction functor
has an exact left adjoint, namely extension by zero in the localized site.

*Step 2: degrees $q\geq2$.* The two standard affine charts
$U,V\subset \mathbf P^1_R$ have affine intersection, so
(4.11) shows that the restriction of $I$
to each of $U_0$, $V_0$ and $(U\cap V)_0$ has no cohomology in positive
degrees. The Mayer–Vietoris sequence on $\mathbf P^1_\kappa$ therefore gives
$H^q(\mathbf P^1_\kappa,I_0)=0$ for $q\geq2$ (this is the case of two
charts in [Stacks, [0A51](https://stacks.math.columbia.edu/tag/0A51)]). In degree one the same sequence only identifies
$H^1(\mathbf P^1_\kappa,I_0)$ with the cokernel of
$\Gamma(U_0,I_0)\oplus\Gamma(V_0,I_0)\to\Gamma((U\cap V)_0,I_0)$, and
nothing said so far shows that this cokernel vanishes.

*Step 3: degree one.* Let $\xi\in H^1(\mathbf P^1_\kappa,I_0)$. Following
[Stacks, [0A5H](https://stacks.math.columbia.edu/tag/0A5H)], we show that $\xi=0$. First write $I$ as a filtered
colimit of constructible $\mathbf F_\ell$-sheaves. Since pullback and $H^1$ on
$\mathbf P^1_\kappa$ commute with this colimit, $\xi$ is the image of a
class $\zeta\in H^1(\mathbf P^1_\kappa,G_0)$ for some constructible $G$ with a map
$G\to I$. Next choose (4.9) and put
$P=\bigoplus_a(h_a)_*\underline{M_a}$. Since $I$ is injective, the map
$G\to I$ extends to $P\to I$. Let $\zeta'$ be the image of $\zeta$ in
$H^1(\mathbf P^1_\kappa,P_0)$.

The class $\zeta'$ lifts to $H^1(\mathbf P^1_R,P)$. Indeed,
(4.10) and the Leray spectral sequence give

$$
H^1(\mathbf P^1_\kappa,P_0)
\simeq\bigoplus_a H^1((Y_a)_0,\underline{M_a}),\qquad
H^1(\mathbf P^1_R,P)\simeq\bigoplus_a H^1(Y_a,\underline{M_a}).
$$

Each $Y_a$ is finite over $\mathbf P^1_R$, hence proper over $R$, so the
comparison (4.8) for finite torsors
(Theorem [theorem-finite-etale-covers-proper-henselian])
lifts $\zeta'$. This lift maps to zero in $H^1(\mathbf P^1_R,I)$ because
$I$ is injective. Now the commutative square of restriction maps

$$
\begin{CD}
H^1(\mathbf P^1_R,P) @>>> H^1(\mathbf P^1_R,I)\\
@VVV @VVV\\
H^1(\mathbf P^1_\kappa,P_0) @>>> H^1(\mathbf P^1_\kappa,I_0)
\end{CD}
$$

shows that the image of $\zeta'$ in $H^1(\mathbf P^1_\kappa,I_0)$ is zero, and this image is $\xi$, because $G\to P\to I$ is the given map $G\to I$.
Hence $\xi=0$.
