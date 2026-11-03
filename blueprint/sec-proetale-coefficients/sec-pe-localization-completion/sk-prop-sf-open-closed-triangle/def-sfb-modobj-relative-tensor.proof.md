+++
kind  = "proof"
of    = "def-sfb-modobj-relative-tensor"
+++
For a monoid object $A$, the $A$-$A$-bimodules form a monoidal category under $\otimes_A$
with unit $A$. The associativity and unit isomorphisms descend from those of $\mathcal C$
to the coequalizers because $\otimes$ preserves coequalizers in each variable. By
[lem-sfb-symmetric-bimod-tensor], the symmetric $\mathcal R$-$\mathcal R$-bimodules are
closed under $\otimes_{\mathcal R}$. The regular bimodule $\mathcal R$ is symmetric because
$\mathcal R$ is commutative, i.e. $\mu\beta_{\mathcal R,\mathcal R}=\mu$. By
[lem-sfb-modobj-symmetric-bimodules], $\Mod_{\mathcal R}(\mathcal C)$ maps fully faithfully
to the symmetric bimodules. By [def-sfb-symmetric-bimod-module-iso], every symmetric
bimodule, in particular every $\otimes_{\mathcal R}$-product of bimodules attached to module
objects and the unit $\mathcal R$, is isomorphic to the bimodule attached to a module object
with the same underlying object. A monoidal structure therefore transports along this fully
faithful functor. The restricted structure is the one on
$\Mod_{\mathcal R}(\mathcal C)$, and its tensor product is the displayed coequalizer.
