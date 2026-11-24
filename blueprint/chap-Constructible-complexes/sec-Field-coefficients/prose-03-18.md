+++
id = "prose-03-18"
kind = "hidden"
title = "Field coefficients (1)"
order = 258
+++
Until the end of this section, $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, so that
$D^b_{\mathrm{ctf}}=\Dbc$ and we can argue with [constructible](@definition-constructible-sheaves) cohomology sheaves
and standard truncations. Recall (after
Definition [definition-lisse-sheaves]) that a $\Lambda_X$-module is
[constructible](@definition-constructible-sheaves) exactly when it is [lisse](@definition-lisse-sheaves), that is locally free of
finite rank for the [pro-étale topology](@definition-small-pro-etale-site), on each stratum of a finite
stratification of $X$. By dévissage we reduce statements about
[$\Dbc(X,\Lambda)$](@definition-constructible-sheaves) to the simplest [constructible sheaves](@definition-constructible-sheaves), namely [lisse sheaves](@definition-lisse-sheaves)
extended by zero from a stratum, the sheaves $a_!L$ of
Section [sec-Derived-functors]. This dévissage first splits a complex into its
cohomology sheaves by truncation, and then filters each [constructible sheaf](@definition-constructible-sheaves) by
strata.

For this dévissage we need [constructible sheaves](@definition-constructible-sheaves) to form an
abelian category (Lemma [lemma-constructible-sheaves]). In the proof we
reduce a morphism of [lisse](@definition-lisse-sheaves) $E$-sheaves to a morphism of integral lattices,
and for $\overline{\mathbf Q}_\ell$ we first descend the morphism to a finite $E$. To prepare for this, in the next two
lemmas we construct the lattices locally and carry out the descent.
