+++
id = "lemma-coherent-base-change-invertible-sheaves"
kind = "lemma"
title = "Coherent base change for invertible sheaves"
order = 1530
lean = ["AlgebraicGeometry.Scheme.Modules.exists_isFiniteFreeComplex_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree"]
+++
Let $T$ be a $k$-scheme and let $\mathcal L$ be invertible on $C_T$. Then
$Rf_{T,*}\mathcal L$ is locally represented
by a bounded complex of finite locally free $\mathcal O_T$-modules.
For any $a:T'\to T$, the base change map
$La^*Rf_{T,*}\mathcal L\to Rf_{T',*}\mathcal L_{T'}$ is an isomorphism
in the derived category of $\mathcal O_{T'}$-modules. The locus where this complex is an
invertible module in degree $0$ is open. On this locus, $f_{T,*}\mathcal L$ is
invertible, its formation commutes with arbitrary base change, and
$R^1f_{T,*}\mathcal L=0$.
