+++
id = "det-sf-determination-localizing"
kind = "lemma"
title = "Invertibility propagates to the localizing closure"
uses = ["lem-sf-triangle-two-out-of-three", "lem-sf-generating-class-determination"]
+++
Let $\mathcal T,\mathcal T'$ be triangulated categories with arbitrary direct
sums, let $\mathcal S\subset\mathcal T$ be a class of objects, and let
$\Loc(\mathcal S)$ be the smallest full triangulated subcategory of
$\mathcal T$ containing $\mathcal S$ and closed under arbitrary direct sums.
Let $F_1,F_2:\mathcal T\to\mathcal T'$ (or $\Loc(\mathcal S)\to\mathcal T'$)
be exact functors preserving direct sums and $\eta:F_1\to F_2$ a natural
transformation of exact functors, i.e. compatible with the shift
isomorphisms. Then the full subcategory

$$
\mathcal C_\eta=\{K\ :\ \eta_K\text{ is an isomorphism}\}
$$

is a triangulated subcategory closed under arbitrary direct sums (and under
direct summands). Consequently, if $\mathcal S\subset\mathcal C_\eta$, then
$\Loc(\mathcal S)\subset\mathcal C_\eta$.
