+++
kind = "proof"
of = "theorem-smooth-base-change-classical-torsion-2--1"
order = 693002
uses = ["theorem-smooth-base-change-classical-torsion"]
+++
For a sheaf $F$ placed in degree zero, the cohomology maps of the
derived base change map are the degreewise maps of
[theorem-smooth-base-change-classical-torsion], in its étale
$\Lambda$-module formulation. They are isomorphisms in nonnegative
degrees by smooth base change, and in negative degrees both sides
vanish. Hence the derived map is an isomorphism on such a sheaf.

The two functors $g^*Rf_*$ and $Rf'_*g'^*$ are triangulated, and the
base change map commutes with shifts. For a complex with cohomology
in a finite interval, induction along the truncation triangles reduces
the assertion to the preceding sheaf case. At each step the last
term is a cohomology sheaf placed in its degree, and two-out-of-three
gives the result for the middle term.

Now choose $a$ with $K\in D^{\geq a}$. Both functors preserve
$D^{\geq a}$: inverse image is exact and right derived direct image
does not lower cohomological degrees. Thus both sides have zero
cohomology in degrees below $a$. For $i\geq a$, apply the two functors
to the truncation triangle

$$
\tau_{\leq i}K\longrightarrow K\longrightarrow
\tau_{\geq i+1}K\longrightarrow (\tau_{\leq i}K)[1].
$$

The image of the third term has no cohomology below $i+1$, so
$\tau_{\leq i}K\to K$ induces an isomorphism on $H^i$ after either
functor. The truncation is bounded, and its relevant cohomology sheaves
satisfy the same torsion condition. Naturality and the bounded case
therefore show that the base change map at $K$ is an isomorphism on
$H^i$. Since this holds in every degree, it is an isomorphism. This is
the dévissage used in `DerivedCategory.Plus.isIso_app_of_forall_homology`.

If a positive integer $n$ kills $\Lambda$ and is invertible on $Y$,
every geometric stalk of every $\Lambda$-module sheaf is killed by $n$.
The hypothesis on the cohomology sheaves is then automatic, as in
`AlgebraicGeometry.Scheme.IsTorsionSheafOfInvertibleOrder.of_natCast_eq_zero`.
