+++
id = "sec-sf-subcategories"
kind = "section"
title = "The constructible finite-Tor subcategories and the six operations"
order = 3757
uses = ["cor-coef-finite-verdier", "cor-coef-integral-internal-hom", "cor-sf-direct-image-ctf-proetale", "cor-weil-finite-constructible-hom", "def-compact-support-direct-image-detailed", "def-sf-datum", "def-weil-derived-complete-integral-detailed", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "def-weil-site-perfect-complex", "lem-coef-finite-direct-image", "lem-coef-finite-exceptional", "lem-coef-integral-hom-reduction", "lem-coef-integral-residue-tor", "lem-coef-rational-operations", "lem-exc-constant-inverse-image-flat", "lem-fix-operation-reduction", "lem-sf-etale-direct-image-vanishing", "lem-weil-pbc-pullback-preserves-bounded-constructible", "open-sf-preservation-gaps", "prop-coef-integral-exceptional-adjoint", "prop-sf-dualizable-hom", "thm-coef-finite-hom", "thm-coef-integral-verdier", "thm-coef-qbar-verdier", "thm-coef-rational-verdier", "thm-fix-general-biduality", "thm-sf-direct-image-tor-amplitude"]
+++
The framework is used on two levels, and the passage between them is not
formal. *Ambient level*: the ordinary derived categories of the
étale and the small pro-étale site, on which the adjunctions, the
exceptional right adjoint and the duality functor are constructed
(def:weil-pbc-derived-categories, the ambient right adjoint of the
exceptional-restriction chapter, and def:weil-ambient-exceptional-adjoint).
*Constructible level*: the bounded constructible finite-Tor
subcategories $D^b_{ctf}$ of def:weil-finite-torsion-constructibility
and def:weil-finite-tor-amplitude, with the cohomological intervals
of def:weil-constructible-intervals, on which the axioms
[def-sf-datum] are stated. Writing down a right adjoint in the ambient
categories does not assert that its values are constructible, so each of the
six operations has to be shown to preserve the constructible level; those
statements are collected here with their individual domains and hypotheses.
They enter [def-sf-datum] only on those verified domains. The convention throughout the blueprint is that general
statements are formulated and proved in the ambient categories and that
their $D^b_{ctf}$ forms are corollaries of the theorem below.
