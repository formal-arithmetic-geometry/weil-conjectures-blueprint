+++
id = "sbc-lem-rel-dim-one-induction"
kind = "lemma"
title = "The induction step in relative dimension one"
order = 1420
uses = ["def-sbc-smooth-morphisms", "sbc-def-base-change-property", "sbc-lem-bc-universal-test", "sbc-thm-universal-test-vanishing"]
+++
Let $f:X\to S$ be an affine smooth morphism of relative dimension one
with $X$ affine, let $n$ be an integer invertible on $S$, and assume
$\mathrm{BC}(f,n,q-1)$ holds for some $q\geq1$ in the sense of
[sbc-def-base-change-property]. Then $\mathrm{BC}(f,n,q)$ holds.

## Proof

Suppose $\mathrm{BC}(f,n,q)$ does not hold. By
[sbc-lem-bc-universal-test] there is a universal
curve test datum: after base
change and normalization, $X'\to S'$ is affine smooth of relative
dimension one, $S'$ is the
spectrum of a normal domain with algebraically closed fraction field
$L$, $K/L$ an extension of algebraically closed fields, and for some
$d\mid n$ the sheaf $R^qh_*(\mathbf Z/d\mathbf Z)$ is nonzero. This
contradicts [sbc-thm-universal-test-vanishing], whose hypotheses
hold: $d$ is invertible on $S'$ because $d\mid n$ and $n$ is invertible
on $S$ and on all its base changes (the $\mathrm{BC}$-property
being a statement about base changes of
$f$); the normalization $S''\to S'$ in $\operatorname{Spec}K$ is
integral because the integral closure of the domain $A'$ in $K$ is
integral over $A'$ (commutative algebra). Hence $\mathrm{BC}(f,n,q)$
holds.
