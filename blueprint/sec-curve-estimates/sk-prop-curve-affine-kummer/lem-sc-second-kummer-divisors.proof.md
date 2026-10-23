+++
kind  = "proof"
of    = "lem-sc-second-kummer-divisors"
uses  = ["lem-sc-kummer-exact"]
+++
*General schemes.* Since $n$ is invertible on $X$, the Kummer sequence is
exact on $X_{\Et}$ ([lem-sc-kummer-exact]). In its long exact cohomology
sequence
$$
H^1(X,\mathbf G_m)\xrightarrow{n}H^1(X,\mathbf G_m)\to H^2(X,\mu_n)\to
H^2(X,\mathbf G_m)\xrightarrow{n}H^2(X,\mathbf G_m)
$$
we have $H^1(X,\mathbf G_m)=\operatorname{Pic}(X)$ ([lem-sc-h1-gm-pic]) and
$H^2(X,\mathbf G_m)=\operatorname{Br}(X)$ ([def-br]). Exactness at the three
middle terms gives the displayed short exact sequence: the kernel of the
coboundary is $n\cdot\operatorname{Pic}(X)$, and the image of
$H^2(X,\mu_n)\to\operatorname{Br}(X)$ is the kernel $\operatorname{Br}(X)[n]$ of
multiplication by $n$.

*Curves.* By [lem-sc-brauer-zero-all-curves], $H^2(C_{\Et},\mathbf G_m)=0$.
This is exactly the hypothesis of [lem-sc-kummer-les]. That lemma
identifies $H^2(C,\mu_n)$ with
$\operatorname{coker}(n:\operatorname{Pic}(C)\to\operatorname{Pic}(C))
=\operatorname{Pic}(C)/n$, via the coboundary of the Kummer sequence
and [lem-sc-h1-gm-pic].
