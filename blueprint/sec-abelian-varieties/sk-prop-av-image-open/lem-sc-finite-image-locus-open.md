+++
id = "lem-sc-finite-image-locus-open"
kind = "lemma"
title = "Finiteness of the image is an open condition on the parameter"
lean = ["AlgebraicGeometry.eventually_finite_image"]
order = 488
+++
Let $k$ be a field, $X$ a $k$-scheme proper over $k$, $Z$ a
$k$-scheme separated and locally of finite type over $k$, $Y$ a
$k$-scheme, $f:X\times_kY\to Z$ a morphism of $k$-schemes and $y_0\in Y$ (an
arbitrary point, not necessarily $k$-rational). For $y\in Y$ write

$$
f_y:X_{\kappa(y)}\longrightarrow Z_{\kappa(y)}
$$

for the fibre over $y$ of $(f,\operatorname{pr}_2):X\times_kY\to Z\times_kY$.
If $f_{y_0}(X_{\kappa(y_0)})$ is finite, then there is an open
neighbourhood $U\subseteq Y$ of $y_0$ such that $f_y(X_{\kappa(y)})$ is
finite for every $y\in U$.
