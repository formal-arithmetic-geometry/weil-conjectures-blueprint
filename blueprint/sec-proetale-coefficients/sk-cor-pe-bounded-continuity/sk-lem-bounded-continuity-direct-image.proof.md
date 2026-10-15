+++
kind  = "proof"
of    = "det-lem-bounded-continuity-direct-image"
+++
For $K$ bounded below, $R^qg_*K$ is the sheaf associated with the presheaf
$V\mapsto H^q(Y\times_ZV,K|_{Y\times_ZV})$ on $Z_{\mathrm{proét}}$ (compute $Rg_*$ with a
K-injective resolution, whose restriction to the object $Y\times_ZV$ of $Y_{\mathrm{proét}}$
computes its cohomology). Affine objects $V$ form a basis of $Z_{\mathrm{proét}}$, so it
suffices to use them. For affine $V$, $Y\times_ZV$ is quasi-compact and quasi-separated
because $g$ is, and restriction to it is exact and commutes with colimits. So by
[det-lem-bounded-continuity-sections] (3) applied on $Y\times_ZV$, the presheaf map
$\varinjlim_iH^q(Y\times_ZV,K_i)\to H^q(Y\times_ZV,\varinjlim_iK_i)$ is an isomorphism for every
affine $V$. Sheafification is a left adjoint, so it commutes with colimits; sheafifying gives
the claim.
