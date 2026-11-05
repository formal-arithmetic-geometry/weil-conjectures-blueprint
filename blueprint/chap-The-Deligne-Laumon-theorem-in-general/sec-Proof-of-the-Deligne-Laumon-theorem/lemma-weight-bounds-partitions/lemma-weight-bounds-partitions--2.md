+++
id = "lemma-weight-bounds-partitions--2"
kind = "lemma"
title = "Weight bounds and partitions (2)"
name_showing = false
order = 1352003
aliases = ["bp-r418-2"]
lean = []
uses = ["definition-weil-structure", "definition-weights", "proposition-construction-independence-rf-shriek"]
+++
This target-partition statement is bypassed by Lean: the general
direct-image bound is assembled by Noetherian induction on the source,
using [lemma-weight-bounds-partitions--1], and by composition with
quasi-finite immersions into the target.

Let $V_0\subset Y_0$ be open with closed complement $W_0$, and let
$f_V$ and $f_W$ be the base changes of $f$ to $V_0$ and $W_0$. If
$R^qf_{V!}(K|_{f^{-1}V_0})$ and $R^qf_{W!}(K|_{f^{-1}W_0})$ are mixed
of weights at most $w+q$ for every $q$, then so is $R^qf_!K$.
