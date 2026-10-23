+++
id = "def-weil-pbc-g-ring"
kind = "definition"
title = "G-ring"
lean = ["IsGRing", "RingHom.IsRegular", "Algebra.IsGeometricallyRegular"]
order = 1649
+++
Let $k$ be a field. A $k$-algebra $A$ is *geometrically regular over $k$* if it is Noetherian and for every finite purely inseparable field extension $k'/k$ the ring $k'\otimes_kA$ is regular, i.e. Noetherian with every localization at a prime ideal a regular local ring (Stacks Project, Algebra, Definition 0382, by condition (2) of Lemma 0381). A ring map $\varphi:R\to\Lambda$ of commutative rings is *regular* if it is flat and for every prime ideal $\mathfrak p\subset R$ the fibre ring $\Lambda\otimes_R\kappa(\mathfrak p)$ is geometrically regular over the residue field $\kappa(\mathfrak p)$ (More on Algebra, Definition 07BZ). A commutative ring $R$ is a *G-ring* if $R$ is Noetherian and for every prime ideal $\mathfrak p\subset R$ the ring map $R_{\mathfrak p}\to(R_{\mathfrak p})^\wedge$ is regular, where $R_{\mathfrak p}$ is the localization of $R$ at $\mathfrak p$, a local ring with maximal ideal $\mathfrak pR_{\mathfrak p}$, and $(R_{\mathfrak p})^\wedge=\varprojlim_nR_{\mathfrak p}/\mathfrak p^nR_{\mathfrak p}$ is its $\mathfrak pR_{\mathfrak p}$-adic completion with its canonical ring map (More on Algebra, Definition 07GH).
