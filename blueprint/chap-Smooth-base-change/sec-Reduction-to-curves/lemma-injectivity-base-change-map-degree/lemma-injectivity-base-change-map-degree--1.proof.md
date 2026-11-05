+++
kind = "proof"
of = "lemma-injectivity-base-change-map-degree--1"
order = 672004
uses = ["definition-derived-base-change-map"]
+++
Choose an embedding $M\hookrightarrow I$ with $I$ injective and put
$Q=I/M$. The short exact sequence gives a distinguished triangle on the
bounded below derived category. Applying $g^*Rf_*$ and $Rf'_*g'^*$ and
taking cohomology gives the two long exact sequences. The derived base
change map commutes with shifts, so it commutes with the connecting maps
as well as with the maps induced by morphisms of sheaves.

Since $q\geq1$ and $I$ is injective, $g^{-1}R^qf_*I=0$. Thus the
upper connecting map $g^{-1}R^{q-1}f_*Q\to g^{-1}R^qf_*M$ is
surjective. The vertical maps on $I$ and $Q$ in degree $q-1$ are
isomorphisms by hypothesis. Comparing the exact sequences identifies
$g^{-1}R^qf_*M$ with the image of the lower connecting map
$R^{q-1}f'_*g'^{-1}Q\to R^qf'_*g'^{-1}M$. The resulting inclusion
into $R^qf'_*g'^{-1}M$ is $b_M^q$, so it is injective.
