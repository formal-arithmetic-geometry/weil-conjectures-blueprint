+++
id = "example-locally-constant-functions-w-local--2"
kind = "example"
title = "The w-local interpretation"
name_showing = false
order = 48002
aliases = ["bp-r009-2"]
lean = []
uses = ["definition-w-local-w-strictly-local", "proposition-pro-etale-site-separably-closed"]
+++
The w-strict locality and w-contractibility conclusions of this example
are bypassed by the Lean route; the spectrum calculation and the
identification of local rings are used directly.

Let $k'$ be a separably closed field, let $S$ be a profinite set, and
put $R=LC(S,k')$. Every point of $\operatorname{Spec}(R)=S$ is closed
and is its own component, so $R$ is w-local and
$\pi_0(\operatorname{Spec}(R))=S$. Its local ring at each $s\in S$ is
$k'$. Thus $R$ is w-strictly local, and it is w-contractible exactly
when $S$ is extremally disconnected, by
[definition-w-local-w-strictly-local]. These are consequences of the
spectrum and local-ring calculations, rather than separate declarations
for $LC(S,k')$ in the mainline.

The assertion that every pro-étale affine over $\operatorname{Spec}k'$
is of this form belongs to
[proposition-pro-etale-site-separably-closed].

*Proof.* The Lean ingredients for the local-ring calculation are the ind-Zariski
facts recalled in [prose-02-10]. The finite products $k'^Q$ are
ind-Zariski over $k'$, so their filtered colimit
$R=LC(S,k')$ is ind-Zariski. Such a map identifies the local ring at
each prime with the local ring at its contraction. Every prime of $R$
contracts to the zero ideal of $k'$, so each local ring is $k'$.

By [example-locally-constant-functions-w-local--1], the spectrum is the
profinite set $S$. Its points are closed singleton components, giving
the w-local assertion and the component space. The local rings are
strictly henselian because $k'$ is separably closed. The remaining
w-strict locality and w-contractibility assertions now follow from the
definitions; this last packaging is not a separate step of the Lean
proof of the main theorem.
