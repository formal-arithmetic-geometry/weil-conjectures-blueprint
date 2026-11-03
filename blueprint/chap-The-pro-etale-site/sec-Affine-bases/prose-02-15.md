+++
id = "prose-02-15"
kind = "hidden"
title = "Affine bases (1)"
order = 65
+++
To compute with sheaves on $X_{\mathrm{pro}\acute{e}t}$ it suffices to evaluate on
affines over which taking sections is exact. Indeed, the refinement
theorem covers every object of $X_{\mathrm{pro}\acute{e}t}$ by pro-étale affines. By the
existence of w-contractible covers, these are in turn covered by such
affines.

The two kinds of affines are used for different purposes. On a
pro-étale affine $U=\varprojlim_iU_i$, a sheaf pulled back from
$X_{\acute{e}t}$ can be evaluated by a colimit. The comparison theorems of
Section [sec-Classical-sheaves] are proved on such affines. On a w-contractible
affine, every epimorphism of sheaves is surjective on sections. The
homological results of the next three subsections are proved there.

In Lemma [lemma-w-contractible-affines-projective] we turn the splitting
of ring maps in Proposition [proposition-splitting-ind-etale-covers]
into a statement about sheaves. The idea is this. A finite cover of a
w-contractible affine has a section. Such a section amounts to a
decomposition of the affine into finitely many clopen pieces, each mapping
into one member of the cover. Local lifts along an epimorphism can then be
glued over these pieces without any further refinement.
