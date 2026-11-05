+++
id = "prose-02-15"
kind = "hidden"
title = "Affine bases (1)"
order = 65
+++
To compute with sheaves on $X_{\mathrm{pro}\acute{e}t}$ it suffices to evaluate on two
kinds of affines. Every object of $X_{\mathrm{pro}\acute{e}t}$ is covered by pro-étale
affines (Theorem [theorem-pro-etale-refinements-weakly-etale]), and
these are in turn covered by w-contractible affines
(Theorem [theorem-existence-contractible-covers]), over which taking
sections is exact.

The two kinds of affines are used for different purposes. On a
pro-étale affine $U=\varprojlim_iU_i$, a sheaf pulled back from
$X_{\acute{e}t}$ can be evaluated by a colimit, and for this reason the comparison theorems of
Section [sec-Classical-sheaves] are proved on such affines. On a w-contractible
affine, by contrast, every epimorphism of sheaves is surjective on sections, so the
homological results of the next three sections are proved there.

In Lemma [lemma-w-contractible-affines-projective] we turn the splitting
of ring maps in Proposition [proposition-splitting-ind-etale-covers]
into a statement about sheaves. The idea is this. A finite cover of a
w-contractible affine has a section. Such a section amounts to a
decomposition of the affine into finitely many clopen pieces, each mapping
into one member of the cover. Local lifts along an epimorphism can then be
glued over these pieces without any further refinement.
