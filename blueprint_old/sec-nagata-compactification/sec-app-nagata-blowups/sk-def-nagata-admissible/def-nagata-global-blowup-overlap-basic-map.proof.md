+++
kind  = "proof"
of    = "def-nagata-global-blowup-overlap-basic-map"
uses = ["def-nagata-global-blowup-local-model", "prop-nagata-affine-blowup-restrict"]
+++
We check that $r_{V,U}$ is an open immersion onto
$\mathsf B_V(\mathcal I)|_U$. The transition morphisms are compatible with
the structure morphisms, so $r_{V,U}$ lands in $\mathsf B_V(\mathcal I)|_U$.
If $W=D(s)\subseteq V$ is a basic open of $V$, then $\Gamma(V,\mathcal O_X)\to
\Gamma(W,\mathcal O_X)$ is a localization away from $s$ and
$\Gamma(W,\mathcal I)=\Gamma(V,\mathcal I)\,\Gamma(W,\mathcal O_X)$, so
by [prop-nagata-affine-blowup-restrict] the morphism $r_{V,W}$ is an open
immersion onto $\mathsf B_V(\mathcal I)|_W$. Now cover $U$ by opens $W$ that
are basic opens of $V$ contained in $U$; each is then also a basic open of
$U$. For such $W$ we have $r_{V,W}=r_{V,U}\circ r_{U,W}$ by functoriality
of the local models, and both $r_{V,W}$ and $r_{U,W}$ are isomorphisms onto
the parts over $W$. Hence $r_{V,U}$ maps $\mathsf B_U(\mathcal I)|_W$
isomorphically onto $\mathsf B_V(\mathcal I)|_W$. As the $W$ cover $U$,
$r_{V,U}$ is an open immersion with image $\mathsf B_V(\mathcal I)|_U$.
