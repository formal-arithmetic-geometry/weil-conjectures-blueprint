+++
id = "def-sfb-modobj-extension"
kind = "definition"
title = "Extension of scalars"
order = 1531
uses = ["lem-sfb-modobj-symmetric-bimodules", "sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.extendScalars"]
+++
Let $\mathcal C$ be a braided monoidal category with coequalizers such that $X\otimes-$ and
$-\otimes X$ preserve colimits for every $X$. Let $\varphi\colon\mathcal R\to\mathcal S$ be
a morphism of monoid objects with $\mathcal R$ commutative. Then $\mathcal S$ is an
$\mathcal S$-$\mathcal R$-bimodule: it acts on itself on the left by $\mu_{\mathcal S}$,
and $\mathcal R$ acts on the right by $\mu_{\mathcal S}(\mathcal S\otimes\varphi)$. Every
$\mathcal R$-module object $M$ ([sk-def-sfb-module-objects]) is an
$\mathcal R$-$\mathcal R$-bimodule ([lem-sfb-modobj-symmetric-bimodules]). Their tensor
product over $\mathcal R$,
$$
\mathcal S\otimes_{\mathcal R}M=\operatorname{coeq}\Bigl(\mathcal S\otimes\mathcal R\otimes M
\rightrightarrows\mathcal S\otimes M\Bigr)
$$
of $\bigl(\mu_{\mathcal S}(\mathcal S\otimes\varphi)\bigr)\otimes M$ and
$(\mathcal S\otimes\gamma_M)\alpha$, is a left $\mathcal S$-module object, with
$\mathcal S$ acting on the first factor. A morphism $f$ goes to the map induced by
$\mathcal S\otimes f$. This defines the *extension of scalars* functor
$\operatorname{Ext}_\varphi\colon\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$.
