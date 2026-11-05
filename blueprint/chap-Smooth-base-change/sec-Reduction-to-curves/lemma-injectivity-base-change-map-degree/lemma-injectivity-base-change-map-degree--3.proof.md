+++
kind = "proof"
of = "lemma-injectivity-base-change-map-degree--3"
order = 672006
uses = ["definition-derived-base-change-map"]
+++
Put $Q=I/M$. The source of $b_I^q$ vanishes because $I$ is injective
and $q\geq1$. Naturality therefore shows that
$R^qf'_*g'^{-1}M\to R^qf'_*g'^{-1}I$ kills the image of $b_M^q$,
so it induces a map from the cokernel.

The distinguished triangle of $0\to M\to I\to Q\to0$ gives long
exact sequences after applying $g^*Rf_*$ and $Rf'_*g'^*$. Compatibility
of derived base change with shifts makes the square of connecting maps
commute. The upper connecting map
$g^{-1}R^{q-1}f_*Q\to g^{-1}R^qf_*M$ is surjective, and $b_Q^{q-1}$
is an isomorphism. Hence the image of $b_M^q$ is exactly the image of
the lower connecting map, which by exactness is the kernel of
$R^qf'_*g'^{-1}M\to R^qf'_*g'^{-1}I$. The induced map from the
cokernel is therefore injective.
