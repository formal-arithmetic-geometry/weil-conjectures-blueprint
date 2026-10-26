+++
id = "lem-weil-pbc-free-complex-mod-nonzerodivisor-exact"
kind = "lemma"
title = "Reducing an exact finite free complex modulo a nonzerodivisor keeps exactness one step less"
lean = ["free_complex_mod_nonzerodivisor_exact"]
order = 1795
+++
Let $(R,\mathfrak m)$ be a local ring, $e\ge2$ an integer and $0\to R^{\oplus n_e}\xrightarrow{\varphi_e}R^{\oplus n_{e-1}}\xrightarrow{\varphi_{e-1}}\cdots\xrightarrow{\varphi_1}R^{\oplus n_0}$ a complex of finite free $R$-modules ($\varphi_i\circ\varphi_{i+1}=0$ for $1\le i\le e-1$) which is exact at $R^{\oplus n_e},R^{\oplus n_{e-1}},\dots,R^{\oplus n_1}$. Let $x\in\mathfrak m$ be a nonzerodivisor of $R$ ($xy=0$ implies $y=0$), $\bar R=R/xR$, and $\bar\varphi_i:\bar R^{\oplus n_i}\to\bar R^{\oplus n_{i-1}}$ the $\bar R$-linear map whose matrix is the matrix of $\varphi_i$ with its entries reduced modulo $x$ (equivalently $\varphi_i\otimes_R\bar R$). Then the complex $0\to\bar R^{\oplus n_e}\xrightarrow{\bar\varphi_e}\bar R^{\oplus n_{e-1}}\to\cdots\xrightarrow{\bar\varphi_2}\bar R^{\oplus n_1}$ is exact at $\bar R^{\oplus n_e},\bar R^{\oplus n_{e-1}},\dots,\bar R^{\oplus n_2}$.
