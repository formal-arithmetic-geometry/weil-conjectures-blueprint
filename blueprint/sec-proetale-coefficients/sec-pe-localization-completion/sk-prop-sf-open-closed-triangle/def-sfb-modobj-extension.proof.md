+++
kind  = "proof"
of    = "def-sfb-modobj-extension"
+++
The bimodule axioms for $\mathcal S$ follow from the associativity and unit laws of
$\mu_{\mathcal S}$, together with $\varphi$ being a morphism of monoid objects. By
[lem-sfb-modobj-symmetric-bimodules], $M$ is a bimodule. Since $\mathcal S\otimes-$
preserves coequalizers,
$$
\mathcal S\otimes(\mathcal S\otimes\mathcal R\otimes M)\rightrightarrows
\mathcal S\otimes(\mathcal S\otimes M)\to\mathcal S\otimes(\mathcal S\otimes_{\mathcal R}M)
$$
is again a coequalizer. The map $\mu_{\mathcal S}\otimes M$ is compatible with both
parallel maps, by associativity of $\mu_{\mathcal S}$. So it descends to an action
$\mathcal S\otimes(\mathcal S\otimes_{\mathcal R}M)\to\mathcal S\otimes_{\mathcal R}M$. The
unit and associativity laws hold because they hold before descending and the projections
are epimorphisms. For an $\mathcal R$-linear $f$, the map $\mathcal S\otimes f$ is
compatible with the two parallel maps. So it descends to an $\mathcal S$-linear map, and
this is functorial.
