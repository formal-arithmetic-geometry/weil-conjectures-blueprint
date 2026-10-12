+++
id = "def-sfb-modobj-relative-tensor"
kind = "definition"
title = "The relative tensor product $\\otimes_{\\mathcal R}$"
order = 1524
uses = ["def-sfb-symmetric-bimod-module-iso", "lem-sfb-modobj-symmetric-bimodules", "lem-sfb-symmetric-bimod-tensor"]
lean = ["CategoryTheory.Mod.monoidalCategory"]
+++
Let $\mathcal C$ be a braided monoidal category with braiding $\beta$ and with
coequalizers, such that $X\otimes-$ and $-\otimes X$ preserve colimits for every $X$. Let
$\mathcal R$ be a commutative monoid object. For $\mathcal R$-module objects $M$ and $N$,
the *relative tensor product* $M\otimes_{\mathcal R}N$ is the tensor product over
$\mathcal R$ ([lem-sfb-symmetric-bimod-tensor]) of the symmetric bimodules attached to $M$
and $N$ ([lem-sfb-modobj-symmetric-bimodules]), viewed as a left module:
$$
M\otimes_{\mathcal R}N=\operatorname{coeq}\Bigl(M\otimes\mathcal R\otimes N
\rightrightarrows M\otimes N\Bigr)
$$
of $(\gamma_M\beta_{M,\mathcal R})\otimes N$ and $(M\otimes\gamma_N)\alpha_{M,\mathcal R,N}$,
with $\mathcal R$ acting through $M$. With unit the regular module $\mathcal R$, and with
the associator and unitors induced from those of bimodules, this is a monoidal structure
on $\Mod_{\mathcal R}(\mathcal C)$.
