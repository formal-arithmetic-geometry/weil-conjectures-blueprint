+++
id = "lemma-cycle-class-cartier-divisor"
kind = "lemma"
title = "The cycle class of a Cartier divisor"
order = 543
lean = ["AlgebraicGeometry.ProEtale.exists_geoCartierCycleClass", "AlgebraicGeometry.ProEtale.geoCartierCanonicalClass"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
Let $\Lambda$ be a finite commutative $\ell$-primary ring, and let
$i:D\hookrightarrow Z$ be an effective Cartier divisor on a
scheme $Z$ on which $\ell$ is invertible. There is a morphism

$$
c_D:i_*\Lambda_D\longrightarrow\Lambda_Z(1)[2]\quad\text{in }D(Z_{\acute{e}t},\Lambda),
$$

and hence, via $\nu_Z^*$, in $D(Z_{\mathrm{pro}\acute{e}t},\Lambda)$,
whose composite with $\Lambda_Z\to i_*\Lambda_D$ is the Kummer first
Chern class $c_1(\mathcal O_Z(D))$. It is compatible with change of
coefficients and with every base change along which the pullback of the
divisor is still an effective Cartier divisor.
