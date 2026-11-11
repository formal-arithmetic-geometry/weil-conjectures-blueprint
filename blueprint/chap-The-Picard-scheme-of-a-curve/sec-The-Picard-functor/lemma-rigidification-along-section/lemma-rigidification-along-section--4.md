+++
id = "lemma-rigidification-along-section--4"
kind = "lemma"
title = "Rigidification along a section (4)"
name_showing = false
order = 1523007
aliases = ["bp-r474-4"]
lean = ["AlgebraicGeometry.picardFunctorNormalized_eq_of_iso_tensorObj"]
uses = ["definition-relative-picard-functor"]
+++
Let $f:C\to S$ have a section $\sigma:S\to C$. For an invertible sheaf
$\mathcal L$ on $C_T$, its normalization is

$$
\mathcal L\longmapsto
\mathcal L\otimes f_T^*(\sigma_T^*\mathcal L)^{-1}.
$$

Its pullback along $\sigma_T$ is trivial. This construction needs no
condition $(\ast)$.

Normalized classes are determined by their twists in the following
sense. Let $\mathcal L,\mathcal L'$ be invertible sheaves on $C_T$ with
trivial pullback along $\sigma_T$. If an $\mathcal O_{C_T}$-module
$\mathcal P$ and $\mathcal O_T$-modules $\mathcal N,\mathcal N'$ admit
isomorphisms

$$
\mathcal L\simeq\mathcal P\otimes f_T^*\mathcal N,
\qquad
\mathcal L'\simeq\mathcal P\otimes f_T^*\mathcal N',
$$

then $[\mathcal L]=[\mathcal L']$ in $\operatorname{Pic}(C_T)$.
No invertibility assumption on $\mathcal P,\mathcal N,\mathcal N'$ and
no condition $(\ast)$ are required.
