+++
id = "definition-change-of-coefficients-maps"
kind = "definition"
title = "Change-of-coefficients maps"
order = 625
+++
Let $\Lambda\to\Lambda'$ be one of the maps listed above, and let
$f:X\to Y$ be a morphism of schemes of finite type over $k$.

1. For $K\in D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$, the isomorphism
   $(f^*K)_{\Lambda'}\simeq f^*(K_{\Lambda'})$ is the one given by
   associativity of derived pullback for ringed topoi [Stacks, [06YV](https://stacks.math.columbia.edu/tag/06YV)]: both
   sides are the derived pullback along the morphism of ringed topoi
   $(X_{\mathrm{pro}\acute{e}t},\Lambda'_X)\to(Y_{\mathrm{pro}\acute{e}t},\Lambda_Y)$, factored in the two
   possible ways.
2. For an open immersion $j:U\to X$ and $K\in D(U_{\mathrm{pro}\acute{e}t},\Lambda)$,
   the isomorphism $(j_!K)_{\Lambda'}\simeq j_!(K_{\Lambda'})$ is the
   isomorphism of left adjoints corresponding to the equality of their right
   adjoints, restriction of scalars followed by $j^*$ and $j^*$ followed by
   restriction of scalars.
3. For $K,L\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the isomorphism
   $(K\otimes^{\mathbf L}_\Lambda L)_{\Lambda'}\simeq
  K_{\Lambda'}\otimes^{\mathbf L}_{\Lambda'}L_{\Lambda'}$ is the
   associativity isomorphism: both sides are
   $K\otimes^{\mathbf L}_\Lambda L\otimes^{\mathbf L}_\Lambda\Lambda'$.
4. For $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the map
   $(Rf_*K)_{\Lambda'}\to Rf_*(K_{\Lambda'})$ is the adjoint transpose, under
   $f^*\dashv Rf_*$ on $D(-_{\mathrm{pro}\acute{e}t},\Lambda')$, of
   $$
   f^*\bigl((Rf_*K)_{\Lambda'}\bigr)\simeq(f^*Rf_*K)_{\Lambda'}
   \xrightarrow{(\varepsilon_K)_{\Lambda'}}K_{\Lambda'},
   $$
   where the first arrow is the inverse of (1) and $\varepsilon$ is the counit of
   $f^*\dashv Rf_*$ on $D(-_{\mathrm{pro}\acute{e}t},\Lambda)$.
5. If $f$ is separated, $f=p\circ j$ is a compactification and
   $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the map
   $(Rf_!K)_{\Lambda'}\to Rf_!(K_{\Lambda'})$ is the composite
   $$
   (Rp_*j_!K)_{\Lambda'}\longrightarrow Rp_*\bigl((j_!K)_{\Lambda'}\bigr)
   \simeq Rp_*j_!(K_{\Lambda'})
   $$
   of (4) for $p$ and $Rp_*$ of (2).
6. For $K,L\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the map
   $\cHom(K,L)_{\Lambda'}\to\cHom(K_{\Lambda'},L_{\Lambda'})$ is the
   adjoint transpose, under $-\otimes^{\mathbf L}K_{\Lambda'}\dashv
  \cHom(K_{\Lambda'},-)$, of
   $$
   \cHom(K,L)_{\Lambda'}\otimes^{\mathbf L}_{\Lambda'}K_{\Lambda'}
   \simeq\bigl(\cHom(K,L)\otimes^{\mathbf L}_\Lambda K\bigr)_{\Lambda'}
   \xrightarrow{(\mathrm{ev})_{\Lambda'}}L_{\Lambda'},
   $$
   where the first arrow is the inverse of (3) and $\mathrm{ev}$ is evaluation.
