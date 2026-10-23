+++
id = "def-sc-ample"
kind = "definition"
title = "Very ample and ample line bundles"
lean = ["AlgebraicGeometry.IsVeryAmple", "AlgebraicGeometry.IsAmple"]
order = 463
+++
Let $X$ be a scheme over a field $k$ and $\mathcal L$ an
$\mathcal O_X$-module. $\mathcal L$ is *very ample* if there are an
integer $N\ge0$ and a closed immersion $i:X\hookrightarrow\mathbf P^N_k$
over $k$ with $i^*\mathcal O(1)\cong\mathcal L$. $\mathcal L$ is
*ample* if it is invertible and $\mathcal L^{\otimes m}$ is very ample for
some $m\geq1$.

For $X$ proper over $k$ and $\mathcal L$ invertible, this is the standard
notion of an ample invertible sheaf.
