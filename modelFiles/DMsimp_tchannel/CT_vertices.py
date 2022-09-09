# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 31 Oct 2019 12:23:25


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_244_91,(0,0,1):C.R2GC_244_92})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,1,0):C.R2GC_239_86,(0,1,1):C.R2GC_239_87,(2,1,0):C.R2GC_239_86,(2,1,1):C.R2GC_239_87,(5,1,0):C.R2GC_237_82,(5,1,1):C.R2GC_237_83,(1,1,0):C.R2GC_237_82,(1,1,1):C.R2GC_237_83,(7,1,0):C.R2GC_247_97,(7,1,1):C.R2GC_247_98,(4,1,0):C.R2GC_237_82,(4,1,1):C.R2GC_237_83,(3,1,0):C.R2GC_237_82,(3,1,1):C.R2GC_237_83,(8,1,0):C.R2GC_238_84,(8,1,1):C.R2GC_238_85,(6,1,0):C.R2GC_246_95,(6,1,1):C.R2GC_246_96,(11,0,0):C.R2GC_241_89,(11,0,1):C.R2GC_241_90,(10,0,0):C.R2GC_241_89,(10,0,1):C.R2GC_241_90,(9,0,1):C.R2GC_240_88,(0,2,0):C.R2GC_239_86,(0,2,1):C.R2GC_239_87,(2,2,0):C.R2GC_239_86,(2,2,1):C.R2GC_239_87,(5,2,0):C.R2GC_237_82,(5,2,1):C.R2GC_237_83,(1,2,0):C.R2GC_237_82,(1,2,1):C.R2GC_237_83,(7,2,0):C.R2GC_247_97,(7,2,1):C.R2GC_238_85,(6,2,0):C.R2GC_252_99,(6,2,1):C.R2GC_252_100,(4,2,0):C.R2GC_237_82,(4,2,1):C.R2GC_237_83,(3,2,0):C.R2GC_237_82,(3,2,1):C.R2GC_237_83,(8,2,0):C.R2GC_238_84,(8,2,1):C.R2GC_247_98,(0,3,0):C.R2GC_239_86,(0,3,1):C.R2GC_239_87,(2,3,0):C.R2GC_239_86,(2,3,1):C.R2GC_239_87,(5,3,0):C.R2GC_237_82,(5,3,1):C.R2GC_237_83,(1,3,0):C.R2GC_237_82,(1,3,1):C.R2GC_237_83,(7,3,0):C.R2GC_245_93,(7,3,1):C.R2GC_245_94,(4,3,0):C.R2GC_237_82,(4,3,1):C.R2GC_237_83,(3,3,0):C.R2GC_237_82,(3,3,1):C.R2GC_237_83,(8,3,0):C.R2GC_238_84,(8,3,1):C.R2GC_245_94,(6,3,0):C.R2GC_246_95})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_256_102})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_263_106})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_263_106})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_263_106})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_263_106})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_263_106})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_263_106})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_560_184})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_725_203})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_547_171})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_560_184})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_725_203})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_547_171})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_743_211})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_556_180})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_736_208})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_743_211})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_556_180})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_736_208})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_729_204})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_458_155})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_457_154})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_560_184})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_725_203})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_547_171})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_560_184})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_725_203})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_547_171})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_743_211})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_556_180})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_736_208})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_743_211})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_556_180})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_736_208})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_562_186})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_554_178})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_549_173})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_257_103})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_552_176})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_275_110})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_557_181})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_557_181})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_277_112})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_557_181})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_557_181})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_276_111})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_278_113})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_275_110,(0,1,0):C.R2GC_288_124})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_722_201})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_722_201})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_722_201})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_722_201})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_276_111})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_278_113})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_275_110,(0,1,0):C.R2GC_288_124})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_544_168})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_544_168})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_544_168})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_544_168})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_276_111})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_278_113})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_275_110,(0,1,0):C.R2GC_288_124})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_624_197,(0,1,0):C.R2GC_622_196})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_622_196,(0,1,0):C.R2GC_624_197})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_276_111})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_620_194,(0,0,1):C.R2GC_620_195})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_278_113})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_275_110,(0,1,0):C.R2GC_288_124})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_624_197,(0,1,0):C.R2GC_622_196})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_622_196,(0,1,0):C.R2GC_624_197})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_276_111})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_620_194,(0,0,1):C.R2GC_620_195})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_278_113})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_275_110,(0,1,0):C.R2GC_288_124})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_624_197,(0,1,0):C.R2GC_622_196})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_622_196,(0,1,0):C.R2GC_624_197})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_276_111})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_620_194,(0,0,1):C.R2GC_620_195})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_278_113})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135,(0,1,0):C.R2GC_364_136})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112,(0,1,0):C.R2GC_291_125})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_558_182})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_620_194,(0,0,0):C.R2GC_620_195})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_550_174})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_620_194,(0,0,0):C.R2GC_620_195})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_545_169})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_626_198})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_627_199,(0,0,1):C.R2GC_627_200})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_620_194,(0,0,0):C.R2GC_620_195})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_739_209})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_739_209})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_739_209})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_739_209})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_551_175})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_551_175})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_551_175})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_551_175})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_363_135})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_732_206})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_732_206})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_277_112})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_732_206})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_732_206})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_365_137})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_368_138})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_281_117,(2,0,1):C.R2GC_281_118,(1,0,0):C.R2GC_281_117,(1,0,1):C.R2GC_281_118,(0,0,0):C.R2GC_241_90,(0,0,1):C.R2GC_280_116})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_730_205})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_259_105})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_259_105})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_259_105})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_266_108})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_266_108})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_266_108})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_283_120})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_284_121})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_285_122})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_283_120})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_284_121})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_285_122})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_283_120})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_284_121})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_285_122})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_328_129})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_329_130})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_330_131})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_328_129})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_329_130})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_330_131})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_328_129})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_329_130})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_330_131})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_373_140})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_374_141})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_375_142})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_373_140})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_374_141})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_375_142})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_373_140})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_617_193})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_374_141})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_375_142})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_412_147})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_413_148})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_414_149})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_412_147})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_413_148})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_414_149})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_412_147})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_413_148})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_414_149})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_286_123})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_286_123})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_286_123})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_331_132})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_331_132})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_331_132})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_376_143})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_376_143})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_376_143})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_415_150})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_415_150})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_415_150})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_263_106})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_263_106})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_263_106})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_256_102})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_256_102})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_256_102})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_257_103})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_552_176})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107,(0,1,0):C.R2GC_266_108})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107,(0,1,0):C.R2GC_266_108})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_265_107,(0,1,0):C.R2GC_266_108})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104,(0,1,0):C.R2GC_259_105})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104,(0,1,0):C.R2GC_259_105})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_258_104,(0,1,0):C.R2GC_259_105})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_561_185})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_553_177})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_172})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_559_183})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_724_202})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_546_170})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_742_210})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_555_179})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_735_207})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_559_183})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_724_202})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_546_170})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_742_210})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_555_179})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_735_207})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_559_183})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_724_202})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_546_170})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_742_210})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_555_179})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_735_207})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_559_183})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_724_202})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_546_170})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_742_210})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_555_179})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_735_207})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_255_101})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_255_101})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_454_153,(0,1,0):C.R2GC_255_101})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_255_101})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_255_101})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_255_101})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_505_162,(0,1,0):C.R2GC_255_101})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_514_163,(0,1,0):C.R2GC_255_101})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_523_164,(0,1,0):C.R2GC_255_101})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_484_159,(0,1,0):C.R2GC_255_101})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_491_160,(0,1,0):C.R2GC_255_101})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_498_161,(0,1,0):C.R2GC_255_101})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_532_165,(0,1,0):C.R2GC_255_101})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_537_166,(0,1,0):C.R2GC_255_101})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_542_167,(0,1,0):C.R2GC_255_101})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_469_156,(0,1,0):C.R2GC_255_101})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_474_157,(0,1,0):C.R2GC_255_101})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_479_158,(0,1,0):C.R2GC_255_101})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,1):C.R2GC_109_1,(0,0,2):C.R2GC_118_13,(0,0,3):C.R2GC_118_14,(0,0,4):C.R2GC_118_15,(0,0,5):C.R2GC_118_16,(0,0,6):C.R2GC_118_17,(0,0,7):C.R2GC_118_18,(0,0,8):C.R2GC_118_19,(0,0,9):C.R2GC_118_20,(0,0,10):C.R2GC_118_21,(0,0,11):C.R2GC_118_22,(0,0,12):C.R2GC_118_23,(0,0,13):C.R2GC_118_24,(0,0,14):C.R2GC_118_25,(0,1,0):C.R2GC_115_8})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_372_139,(0,1,0):C.R2GC_274_109})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_385_144,(0,1,0):C.R2GC_274_109})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_398_145,(0,1,0):C.R2GC_274_109})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_327_128,(0,1,0):C.R2GC_274_109})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_342_133,(0,1,0):C.R2GC_274_109})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_357_134,(0,1,0):C.R2GC_274_109})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_411_146,(0,1,0):C.R2GC_274_109})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_424_151,(0,1,0):C.R2GC_274_109})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_437_152,(0,1,0):C.R2GC_274_109})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_282_119,(0,1,0):C.R2GC_274_109})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_297_126,(0,1,0):C.R2GC_274_109})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_312_127,(0,1,0):C.R2GC_274_109})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_113_4,(0,0,1):C.R2GC_113_5})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_110_2})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_123_53,(0,0,1):C.R2GC_123_54,(0,0,2):C.R2GC_123_55,(0,0,3):C.R2GC_123_56,(0,0,4):C.R2GC_123_57,(0,0,5):C.R2GC_123_58,(0,0,6):C.R2GC_123_59,(0,0,7):C.R2GC_123_60,(0,0,8):C.R2GC_123_61})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_122_44,(0,0,1):C.R2GC_122_45,(0,0,2):C.R2GC_122_46,(0,0,3):C.R2GC_122_47,(0,0,4):C.R2GC_122_48,(0,0,5):C.R2GC_122_49,(0,0,6):C.R2GC_122_50,(0,0,7):C.R2GC_122_51,(0,0,8):C.R2GC_122_52})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_122_44,(0,0,1):C.R2GC_122_45,(0,0,2):C.R2GC_122_46,(0,0,3):C.R2GC_122_47,(0,0,4):C.R2GC_122_48,(0,0,5):C.R2GC_122_49,(0,0,6):C.R2GC_122_50,(0,0,7):C.R2GC_122_51,(0,0,8):C.R2GC_122_52})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xw__tilde__, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_122_44,(0,0,1):C.R2GC_122_45,(0,0,2):C.R2GC_122_46,(0,0,3):C.R2GC_122_47,(0,0,4):C.R2GC_122_48,(0,0,5):C.R2GC_122_49,(0,0,6):C.R2GC_122_50,(0,0,7):C.R2GC_122_51,(0,0,8):C.R2GC_122_52})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_116_9,(0,0,1):C.R2GC_116_10})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_119_26,(0,0,1):C.R2GC_119_27,(0,0,2):C.R2GC_119_28,(0,0,3):C.R2GC_119_29,(0,0,4):C.R2GC_119_30,(0,0,5):C.R2GC_119_31})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_121_38,(0,0,1):C.R2GC_121_39,(0,0,2):C.R2GC_121_40,(0,0,3):C.R2GC_121_41,(0,0,4):C.R2GC_121_42,(0,0,5):C.R2GC_121_43})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_126_80,(0,0,1):C.R2GC_126_81})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_117_11,(0,0,1):C.R2GC_117_12})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_114_6,(1,0,1):C.R2GC_114_7,(0,1,0):C.R2GC_120_32,(0,1,1):C.R2GC_120_33,(0,1,2):C.R2GC_120_34,(0,1,3):C.R2GC_120_35,(0,1,4):C.R2GC_120_36,(0,1,5):C.R2GC_120_37})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_111_3})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_111_3})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_111_3})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_125_71,(0,0,1):C.R2GC_125_72,(0,0,2):C.R2GC_125_73,(0,0,3):C.R2GC_125_74,(0,0,4):C.R2GC_125_75,(0,0,5):C.R2GC_125_76,(0,0,6):C.R2GC_125_77,(0,0,7):C.R2GC_125_78,(0,0,8):C.R2GC_125_79})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_124_62,(0,0,1):C.R2GC_124_63,(0,0,2):C.R2GC_124_64,(0,0,3):C.R2GC_124_65,(0,0,4):C.R2GC_124_66,(0,0,5):C.R2GC_124_67,(0,0,6):C.R2GC_124_68,(0,0,7):C.R2GC_124_69,(0,0,8):C.R2GC_124_70})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_124_62,(0,0,1):C.R2GC_124_63,(0,0,2):C.R2GC_124_64,(0,0,3):C.R2GC_124_65,(0,0,4):C.R2GC_124_66,(0,0,5):C.R2GC_124_67,(0,0,6):C.R2GC_124_68,(0,0,7):C.R2GC_124_69,(0,0,8):C.R2GC_124_70})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_124_62,(0,0,1):C.R2GC_124_63,(0,0,2):C.R2GC_124_64,(0,0,3):C.R2GC_124_65,(0,0,4):C.R2GC_124_66,(0,0,5):C.R2GC_124_67,(0,0,6):C.R2GC_124_68,(0,0,7):C.R2GC_124_69,(0,0,8):C.R2GC_124_70})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_753_219,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_753_221,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_753_219,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_753_221})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_826_287,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_826_289,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_826_291,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_825_281,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_825_283,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_825_285})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_753_219,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_753_221,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_753_219,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_753_221})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_826_287,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_826_289,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_826_291,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_825_281,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_825_283,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_825_285})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_826_287,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_826_289,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_826_291,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_825_281,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_825_283,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_825_285})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_753_219,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_753_221,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_753_219,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_753_221})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,7):C.R2GC_564_191,(1,0,8):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,4):C.R2GC_759_224,(1,0,11):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,5):C.R2GC_820_276,(1,0,10):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_278,(1,0,9):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,7):C.R2GC_563_188,(0,0,8):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,4):C.R2GC_760_227,(0,0,11):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,5):C.R2GC_819_271,(0,0,10):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_273,(0,0,9):C.R2GC_819_274})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_750_216,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_750_217,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_750_216,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_750_217})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,7):C.R2GC_564_191,(1,0,8):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,4):C.R2GC_759_224,(1,0,11):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,5):C.R2GC_820_276,(1,0,10):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_278,(1,0,9):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,7):C.R2GC_563_188,(0,0,8):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,4):C.R2GC_760_227,(0,0,11):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,5):C.R2GC_819_271,(0,0,10):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_273,(0,0,9):C.R2GC_819_274})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_778_251,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_778_252,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_778_253,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_777_248,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_777_249,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_777_250})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_750_216,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_750_217,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_750_216,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_750_217})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_759_224,(1,0,1):C.R2GC_759_225,(1,0,2):C.R2GC_759_226,(0,0,0):C.R2GC_760_227,(0,0,1):C.R2GC_760_228,(0,0,2):C.R2GC_760_229})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_274})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,7):C.R2GC_564_191,(1,0,8):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,4):C.R2GC_759_224,(1,0,11):C.R2GC_820_275,(1,0,1):C.R2GC_782_260,(1,0,5):C.R2GC_820_276,(1,0,10):C.R2GC_820_277,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_820_278,(1,0,9):C.R2GC_820_279,(0,0,3):C.R2GC_563_187,(0,0,7):C.R2GC_563_188,(0,0,8):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,4):C.R2GC_760_227,(0,0,11):C.R2GC_819_270,(0,0,1):C.R2GC_116_9,(0,0,5):C.R2GC_819_271,(0,0,10):C.R2GC_819_272,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_819_273,(0,0,9):C.R2GC_819_274})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_778_251,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_778_252,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_778_253,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_777_248,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_777_249,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_777_250})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_778_251,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_778_252,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_778_253,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_777_248,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_777_249,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_777_250})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_750_216,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_750_217,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_750_216,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_750_217})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_435 = CTVertex(name = 'V_435',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_436 = CTVertex(name = 'V_436',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_437 = CTVertex(name = 'V_437',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_438 = CTVertex(name = 'V_438',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_756_222,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_756_223,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_756_222,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_756_223})

V_439 = CTVertex(name = 'V_439',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_440 = CTVertex(name = 'V_440',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_441 = CTVertex(name = 'V_441',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_442 = CTVertex(name = 'V_442',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_443 = CTVertex(name = 'V_443',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_444 = CTVertex(name = 'V_444',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_445 = CTVertex(name = 'V_445',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_880_305,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_880_306,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_880_307,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_879_302,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_879_303,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_879_304})

V_446 = CTVertex(name = 'V_446',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_756_222,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_756_223,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_756_222,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_756_223})

V_447 = CTVertex(name = 'V_447',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_448 = CTVertex(name = 'V_448',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_449 = CTVertex(name = 'V_449',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_830_295,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_830_296,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_830_297,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_829_292,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_829_293,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_829_294})

V_450 = CTVertex(name = 'V_450',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_451 = CTVertex(name = 'V_451',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_452 = CTVertex(name = 'V_452',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_782_259,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_782_261,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_782_263,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_781_254,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_781_255,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_781_257})

V_453 = CTVertex(name = 'V_453',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_880_305,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_880_306,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_880_307,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_879_302,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_879_303,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_879_304})

V_454 = CTVertex(name = 'V_454',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_826_286,(1,0,8):C.R2GC_880_305,(1,0,1):C.R2GC_826_288,(1,0,7):C.R2GC_880_306,(1,0,2):C.R2GC_826_290,(1,0,6):C.R2GC_880_307,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_825_280,(0,0,8):C.R2GC_879_302,(0,0,1):C.R2GC_825_282,(0,0,7):C.R2GC_879_303,(0,0,2):C.R2GC_825_284,(0,0,6):C.R2GC_879_304})

V_455 = CTVertex(name = 'V_455',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_753_218,(1,0,5):C.R2GC_756_222,(1,0,1):C.R2GC_753_220,(1,0,4):C.R2GC_756_223,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_753_218,(0,0,5):C.R2GC_756_222,(0,0,1):C.R2GC_753_220,(0,0,4):C.R2GC_756_223})

V_456 = CTVertex(name = 'V_456',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_457 = CTVertex(name = 'V_457',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_458 = CTVertex(name = 'V_458',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_459 = CTVertex(name = 'V_459',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_460 = CTVertex(name = 'V_460',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_461 = CTVertex(name = 'V_461',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_462 = CTVertex(name = 'V_462',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_463 = CTVertex(name = 'V_463',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_464 = CTVertex(name = 'V_464',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_465 = CTVertex(name = 'V_465',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_747_213,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_747_215,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_747_213,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_747_215})

V_466 = CTVertex(name = 'V_466',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_467 = CTVertex(name = 'V_467',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_468 = CTVertex(name = 'V_468',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_469 = CTVertex(name = 'V_469',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_470 = CTVertex(name = 'V_470',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_471 = CTVertex(name = 'V_471',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_472 = CTVertex(name = 'V_472',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_473 = CTVertex(name = 'V_473',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_474 = CTVertex(name = 'V_474',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_475 = CTVertex(name = 'V_475',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_766_237,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_766_239,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_766_241,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_765_231,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_765_233,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_765_235})

V_476 = CTVertex(name = 'V_476',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_747_213,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_747_215,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_747_213,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_747_215})

V_477 = CTVertex(name = 'V_477',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_478 = CTVertex(name = 'V_478',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_479 = CTVertex(name = 'V_479',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_814_267,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_814_268,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_814_269,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_813_264,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_813_265,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_813_266})

V_480 = CTVertex(name = 'V_480',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_481 = CTVertex(name = 'V_481',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_482 = CTVertex(name = 'V_482',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_772_245,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_772_246,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_772_247,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_771_242,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_771_243,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_771_244})

V_483 = CTVertex(name = 'V_483',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_484 = CTVertex(name = 'V_484',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_485 = CTVertex(name = 'V_485',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_782_258,(1,0,8):C.R2GC_874_299,(1,0,1):C.R2GC_782_260,(1,0,7):C.R2GC_874_300,(1,0,2):C.R2GC_782_262,(1,0,6):C.R2GC_874_301,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_747_212,(0,0,8):C.R2GC_747_213,(0,0,1):C.R2GC_116_9,(0,0,7):C.R2GC_121_40,(0,0,2):C.R2GC_781_256,(0,0,6):C.R2GC_873_298})

V_486 = CTVertex(name = 'V_486',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_766_237,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_766_239,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_766_241,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_765_231,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_765_233,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_765_235})

V_487 = CTVertex(name = 'V_487',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_564_190,(1,0,4):C.R2GC_564_191,(1,0,5):C.R2GC_564_192,(1,0,0):C.R2GC_766_236,(1,0,8):C.R2GC_766_237,(1,0,1):C.R2GC_766_238,(1,0,7):C.R2GC_766_239,(1,0,2):C.R2GC_766_240,(1,0,6):C.R2GC_766_241,(0,0,3):C.R2GC_563_187,(0,0,4):C.R2GC_563_188,(0,0,5):C.R2GC_563_189,(0,0,0):C.R2GC_765_230,(0,0,8):C.R2GC_765_231,(0,0,1):C.R2GC_765_232,(0,0,7):C.R2GC_765_233,(0,0,2):C.R2GC_765_234,(0,0,6):C.R2GC_765_235})

V_488 = CTVertex(name = 'V_488',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_279_114,(1,0,3):C.R2GC_279_115,(1,0,0):C.R2GC_747_212,(1,0,5):C.R2GC_747_213,(1,0,1):C.R2GC_747_214,(1,0,4):C.R2GC_747_215,(0,0,2):C.R2GC_279_114,(0,0,3):C.R2GC_279_115,(0,0,0):C.R2GC_747_212,(0,0,5):C.R2GC_747_213,(0,0,1):C.R2GC_747_214,(0,0,4):C.R2GC_747_215})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_244_183,(0,0,1):C.UVGC_244_184,(0,0,2):C.UVGC_244_185,(0,0,3):C.UVGC_244_186,(0,0,4):C.UVGC_244_187,(0,0,5):C.UVGC_244_188,(0,0,6):C.UVGC_244_189,(0,0,7):C.UVGC_244_190,(0,0,8):C.UVGC_244_191,(0,0,9):C.UVGC_244_192,(0,0,10):C.UVGC_244_193,(0,0,11):C.UVGC_244_194,(0,0,12):C.UVGC_244_195,(0,0,13):C.UVGC_244_196,(0,0,14):C.UVGC_244_197,(0,0,15):C.UVGC_244_198,(0,0,16):C.UVGC_244_199,(0,0,17):C.UVGC_244_200,(0,0,18):C.UVGC_244_201,(0,0,19):C.UVGC_244_202,(0,0,20):C.UVGC_244_203,(0,0,21):C.UVGC_244_204,(0,0,22):C.UVGC_244_205,(0,0,23):C.UVGC_244_206,(0,0,24):C.UVGC_244_207,(0,0,25):C.UVGC_244_208,(0,0,26):C.UVGC_244_209,(0,0,27):C.UVGC_244_210,(0,0,28):C.UVGC_244_211,(0,0,29):C.UVGC_244_212,(0,0,30):C.UVGC_244_213,(0,0,31):C.UVGC_244_214})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,1,5):C.UVGC_238_114,(0,1,6):C.UVGC_238_113,(2,1,5):C.UVGC_238_114,(2,1,6):C.UVGC_238_113,(5,1,5):C.UVGC_237_111,(5,1,6):C.UVGC_237_112,(1,1,5):C.UVGC_237_111,(1,1,6):C.UVGC_237_112,(7,1,0):C.UVGC_246_247,(7,1,3):C.UVGC_246_248,(7,1,4):C.UVGC_246_249,(7,1,5):C.UVGC_247_279,(7,1,6):C.UVGC_247_280,(7,1,7):C.UVGC_246_252,(7,1,8):C.UVGC_246_253,(7,1,9):C.UVGC_246_254,(7,1,10):C.UVGC_246_255,(7,1,11):C.UVGC_246_256,(7,1,12):C.UVGC_246_257,(7,1,13):C.UVGC_246_258,(7,1,14):C.UVGC_246_259,(7,1,15):C.UVGC_246_260,(7,1,16):C.UVGC_246_261,(7,1,17):C.UVGC_246_262,(7,1,18):C.UVGC_246_263,(7,1,19):C.UVGC_246_264,(7,1,20):C.UVGC_246_265,(7,1,21):C.UVGC_246_266,(7,1,22):C.UVGC_246_267,(7,1,24):C.UVGC_246_268,(7,1,25):C.UVGC_246_269,(7,1,26):C.UVGC_246_270,(7,1,27):C.UVGC_246_271,(7,1,28):C.UVGC_246_272,(7,1,29):C.UVGC_246_273,(7,1,30):C.UVGC_246_274,(7,1,31):C.UVGC_246_275,(7,1,32):C.UVGC_246_276,(7,1,33):C.UVGC_246_277,(7,1,34):C.UVGC_246_278,(4,1,5):C.UVGC_237_111,(4,1,6):C.UVGC_237_112,(3,1,5):C.UVGC_237_111,(3,1,6):C.UVGC_237_112,(8,1,5):C.UVGC_238_113,(8,1,6):C.UVGC_238_114,(6,1,0):C.UVGC_246_247,(6,1,3):C.UVGC_246_248,(6,1,4):C.UVGC_246_249,(6,1,5):C.UVGC_246_250,(6,1,6):C.UVGC_246_251,(6,1,7):C.UVGC_246_252,(6,1,8):C.UVGC_246_253,(6,1,9):C.UVGC_246_254,(6,1,10):C.UVGC_246_255,(6,1,11):C.UVGC_246_256,(6,1,12):C.UVGC_246_257,(6,1,13):C.UVGC_246_258,(6,1,14):C.UVGC_246_259,(6,1,15):C.UVGC_246_260,(6,1,16):C.UVGC_246_261,(6,1,17):C.UVGC_246_262,(6,1,18):C.UVGC_246_263,(6,1,19):C.UVGC_246_264,(6,1,20):C.UVGC_246_265,(6,1,21):C.UVGC_246_266,(6,1,22):C.UVGC_246_267,(6,1,24):C.UVGC_246_268,(6,1,25):C.UVGC_246_269,(6,1,26):C.UVGC_246_270,(6,1,27):C.UVGC_246_271,(6,1,28):C.UVGC_246_272,(6,1,29):C.UVGC_246_273,(6,1,30):C.UVGC_246_274,(6,1,31):C.UVGC_246_275,(6,1,32):C.UVGC_246_276,(6,1,33):C.UVGC_246_277,(6,1,34):C.UVGC_246_278,(11,0,5):C.UVGC_241_117,(11,0,6):C.UVGC_241_118,(10,0,5):C.UVGC_241_117,(10,0,6):C.UVGC_241_118,(9,0,5):C.UVGC_240_115,(9,0,6):C.UVGC_240_116,(0,2,5):C.UVGC_238_114,(0,2,6):C.UVGC_238_113,(2,2,5):C.UVGC_238_114,(2,2,6):C.UVGC_238_113,(5,2,5):C.UVGC_237_111,(5,2,6):C.UVGC_237_112,(1,2,5):C.UVGC_237_111,(1,2,6):C.UVGC_237_112,(7,2,2):C.UVGC_248_281,(7,2,5):C.UVGC_238_113,(7,2,6):C.UVGC_251_345,(6,2,0):C.UVGC_245_215,(6,2,3):C.UVGC_245_216,(6,2,4):C.UVGC_245_217,(6,2,5):C.UVGC_252_346,(6,2,6):C.UVGC_252_347,(6,2,7):C.UVGC_245_220,(6,2,8):C.UVGC_245_221,(6,2,9):C.UVGC_245_222,(6,2,10):C.UVGC_245_223,(6,2,11):C.UVGC_245_224,(6,2,12):C.UVGC_245_225,(6,2,13):C.UVGC_245_226,(6,2,14):C.UVGC_245_227,(6,2,15):C.UVGC_245_228,(6,2,16):C.UVGC_245_229,(6,2,17):C.UVGC_245_230,(6,2,18):C.UVGC_245_231,(6,2,19):C.UVGC_245_232,(6,2,20):C.UVGC_245_233,(6,2,21):C.UVGC_245_234,(6,2,22):C.UVGC_252_348,(6,2,24):C.UVGC_252_349,(6,2,25):C.UVGC_252_350,(6,2,26):C.UVGC_252_351,(6,2,27):C.UVGC_252_352,(6,2,28):C.UVGC_252_353,(6,2,29):C.UVGC_252_354,(6,2,30):C.UVGC_252_355,(6,2,31):C.UVGC_252_356,(6,2,32):C.UVGC_252_357,(6,2,33):C.UVGC_252_358,(6,2,34):C.UVGC_252_359,(4,2,5):C.UVGC_237_111,(4,2,6):C.UVGC_237_112,(3,2,5):C.UVGC_237_111,(3,2,6):C.UVGC_237_112,(8,2,0):C.UVGC_250_314,(8,2,3):C.UVGC_250_315,(8,2,4):C.UVGC_250_316,(8,2,5):C.UVGC_247_279,(8,2,6):C.UVGC_250_317,(8,2,7):C.UVGC_250_318,(8,2,8):C.UVGC_250_319,(8,2,9):C.UVGC_250_320,(8,2,10):C.UVGC_250_321,(8,2,11):C.UVGC_250_322,(8,2,12):C.UVGC_250_323,(8,2,13):C.UVGC_250_324,(8,2,14):C.UVGC_250_325,(8,2,15):C.UVGC_250_326,(8,2,16):C.UVGC_250_327,(8,2,17):C.UVGC_250_328,(8,2,18):C.UVGC_250_329,(8,2,19):C.UVGC_250_330,(8,2,20):C.UVGC_250_331,(8,2,21):C.UVGC_250_332,(8,2,22):C.UVGC_250_333,(8,2,24):C.UVGC_250_334,(8,2,25):C.UVGC_250_335,(8,2,26):C.UVGC_250_336,(8,2,27):C.UVGC_250_337,(8,2,28):C.UVGC_250_338,(8,2,29):C.UVGC_250_339,(8,2,30):C.UVGC_250_340,(8,2,31):C.UVGC_250_341,(8,2,32):C.UVGC_250_342,(8,2,33):C.UVGC_250_343,(8,2,34):C.UVGC_250_344,(0,3,5):C.UVGC_238_114,(0,3,6):C.UVGC_238_113,(2,3,5):C.UVGC_238_114,(2,3,6):C.UVGC_238_113,(5,3,5):C.UVGC_237_111,(5,3,6):C.UVGC_237_112,(1,3,5):C.UVGC_237_111,(1,3,6):C.UVGC_237_112,(7,3,0):C.UVGC_245_215,(7,3,3):C.UVGC_245_216,(7,3,4):C.UVGC_245_217,(7,3,5):C.UVGC_245_218,(7,3,6):C.UVGC_245_219,(7,3,7):C.UVGC_245_220,(7,3,8):C.UVGC_245_221,(7,3,9):C.UVGC_245_222,(7,3,10):C.UVGC_245_223,(7,3,11):C.UVGC_245_224,(7,3,12):C.UVGC_245_225,(7,3,13):C.UVGC_245_226,(7,3,14):C.UVGC_245_227,(7,3,15):C.UVGC_245_228,(7,3,16):C.UVGC_245_229,(7,3,17):C.UVGC_245_230,(7,3,18):C.UVGC_245_231,(7,3,19):C.UVGC_245_232,(7,3,20):C.UVGC_245_233,(7,3,21):C.UVGC_245_234,(7,3,22):C.UVGC_245_235,(7,3,24):C.UVGC_245_236,(7,3,25):C.UVGC_245_237,(7,3,26):C.UVGC_245_238,(7,3,27):C.UVGC_245_239,(7,3,28):C.UVGC_245_240,(7,3,29):C.UVGC_245_241,(7,3,30):C.UVGC_245_242,(7,3,31):C.UVGC_245_243,(7,3,32):C.UVGC_245_244,(7,3,33):C.UVGC_245_245,(7,3,34):C.UVGC_245_246,(4,3,5):C.UVGC_237_111,(4,3,6):C.UVGC_237_112,(3,3,5):C.UVGC_237_111,(3,3,6):C.UVGC_237_112,(8,3,0):C.UVGC_249_283,(8,3,3):C.UVGC_249_284,(8,3,4):C.UVGC_249_285,(8,3,5):C.UVGC_245_218,(8,3,6):C.UVGC_249_286,(8,3,7):C.UVGC_249_287,(8,3,8):C.UVGC_249_288,(8,3,9):C.UVGC_249_289,(8,3,10):C.UVGC_249_290,(8,3,11):C.UVGC_249_291,(8,3,12):C.UVGC_249_292,(8,3,13):C.UVGC_249_293,(8,3,14):C.UVGC_249_294,(8,3,15):C.UVGC_249_295,(8,3,16):C.UVGC_249_296,(8,3,17):C.UVGC_249_297,(8,3,18):C.UVGC_249_298,(8,3,19):C.UVGC_249_299,(8,3,20):C.UVGC_249_300,(8,3,21):C.UVGC_249_301,(8,3,22):C.UVGC_249_302,(8,3,24):C.UVGC_249_303,(8,3,25):C.UVGC_249_304,(8,3,26):C.UVGC_249_305,(8,3,27):C.UVGC_249_306,(8,3,28):C.UVGC_249_307,(8,3,29):C.UVGC_249_308,(8,3,30):C.UVGC_249_309,(8,3,31):C.UVGC_249_310,(8,3,32):C.UVGC_249_311,(8,3,33):C.UVGC_249_312,(8,3,34):C.UVGC_249_313,(6,3,1):C.UVGC_248_281,(6,3,6):C.UVGC_240_115,(6,3,23):C.UVGC_248_282})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_154_28,(0,2,0):C.UVGC_156_30})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_162_36,(0,2,0):C.UVGC_164_38})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_170_44,(0,2,0):C.UVGC_172_46})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_178_52,(0,2,0):C.UVGC_180_54})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_184_58,(0,2,0):C.UVGC_186_60})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_190_64,(0,2,0):C.UVGC_192_66})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_196_70,(0,2,0):C.UVGC_198_72})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_202_76,(0,2,0):C.UVGC_204_78})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_208_82,(0,2,0):C.UVGC_210_84})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_214_88,(0,2,0):C.UVGC_216_90})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_222_96,(0,2,0):C.UVGC_224_98})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_230_104,(0,2,0):C.UVGC_232_106})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_741_1021,(0,0,1):C.UVGC_562_885})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_741_1021,(0,0,1):C.UVGC_562_885})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_562_884,(0,0,1):C.UVGC_562_885})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_562_884,(0,0,1):C.UVGC_562_885})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_554_863,(0,0,1):C.UVGC_554_864})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_554_863,(0,0,1):C.UVGC_554_864})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_727_990,(0,0,1):C.UVGC_554_864})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_727_990,(0,0,1):C.UVGC_554_864})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_734_1006,(0,0,1):C.UVGC_549_850})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_734_1006,(0,0,1):C.UVGC_549_850})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_549_849,(0,0,1):C.UVGC_549_850})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_549_849,(0,0,1):C.UVGC_549_850})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_560_879,(0,0,1):C.UVGC_560_880})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_725_986,(0,0,1):C.UVGC_725_987})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_547_844,(0,0,1):C.UVGC_547_845})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_560_879,(0,0,1):C.UVGC_560_880})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_725_986,(0,0,1):C.UVGC_725_987})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_547_844,(0,0,1):C.UVGC_547_845})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_743_1025,(0,0,1):C.UVGC_743_1026})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_556_868,(0,0,1):C.UVGC_556_869})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_736_1010,(0,0,1):C.UVGC_736_1011})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_743_1025,(0,0,1):C.UVGC_743_1026})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_556_868,(0,0,1):C.UVGC_556_869})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_736_1010,(0,0,1):C.UVGC_736_1011})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_729_993,(0,0,2):C.UVGC_729_994,(0,0,1):C.UVGC_729_995})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_458_790})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_457_789})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_560_879,(0,0,1):C.UVGC_560_880})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_725_986,(0,0,1):C.UVGC_725_987})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_547_844,(0,0,1):C.UVGC_547_845})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_560_879,(0,0,1):C.UVGC_560_880})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_725_986,(0,0,1):C.UVGC_725_987})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_547_844,(0,0,1):C.UVGC_547_845})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_743_1025,(0,0,1):C.UVGC_743_1026})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_556_868,(0,0,1):C.UVGC_556_869})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_736_1010,(0,0,1):C.UVGC_736_1011})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_743_1025,(0,0,1):C.UVGC_743_1026})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_556_868,(0,0,1):C.UVGC_556_869})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_736_1010,(0,0,1):C.UVGC_736_1011})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_741_1021,(0,0,1):C.UVGC_562_885})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_741_1021,(0,0,1):C.UVGC_562_885})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_562_884,(0,0,1):C.UVGC_562_885})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_562_884,(0,0,1):C.UVGC_562_885})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_554_863,(0,0,1):C.UVGC_554_864})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_554_863,(0,0,1):C.UVGC_554_864})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_727_990,(0,0,1):C.UVGC_554_864})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_727_990,(0,0,1):C.UVGC_554_864})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_734_1006,(0,0,1):C.UVGC_549_850})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_734_1006,(0,0,1):C.UVGC_549_850})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_549_849,(0,0,1):C.UVGC_549_850})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_549_849,(0,0,1):C.UVGC_549_850})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_181_55,(0,2,5):C.UVGC_182_56})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_187_61,(0,2,5):C.UVGC_188_62})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_193_67,(0,2,5):C.UVGC_194_68})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_199_73,(0,2,5):C.UVGC_200_74})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_205_79,(0,2,5):C.UVGC_206_80})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_211_85,(0,2,5):C.UVGC_212_86})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_217_91,(0,2,5):C.UVGC_218_92})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_225_99,(0,2,5):C.UVGC_226_100})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_233_107,(0,2,5):C.UVGC_234_108})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_157_31,(0,2,5):C.UVGC_158_32})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_165_39,(0,2,5):C.UVGC_166_40})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,3,0):C.UVGC_242_119,(0,3,1):C.UVGC_242_120,(0,3,2):C.UVGC_242_121,(0,3,3):C.UVGC_242_122,(0,3,4):C.UVGC_242_123,(0,3,6):C.UVGC_242_124,(0,3,7):C.UVGC_242_125,(0,3,8):C.UVGC_242_126,(0,3,9):C.UVGC_242_127,(0,3,10):C.UVGC_242_128,(0,3,11):C.UVGC_242_129,(0,3,12):C.UVGC_242_130,(0,3,13):C.UVGC_242_131,(0,3,14):C.UVGC_242_132,(0,3,15):C.UVGC_242_133,(0,3,16):C.UVGC_242_134,(0,3,17):C.UVGC_242_135,(0,3,18):C.UVGC_242_136,(0,3,19):C.UVGC_242_137,(0,3,20):C.UVGC_242_138,(0,3,21):C.UVGC_242_139,(0,3,22):C.UVGC_242_140,(0,3,23):C.UVGC_242_141,(0,3,24):C.UVGC_242_142,(0,3,25):C.UVGC_242_143,(0,3,26):C.UVGC_242_144,(0,3,27):C.UVGC_242_145,(0,3,28):C.UVGC_242_146,(0,3,29):C.UVGC_242_147,(0,3,30):C.UVGC_242_148,(0,3,31):C.UVGC_242_149,(0,3,32):C.UVGC_242_150,(0,1,5):C.UVGC_173_47,(0,2,5):C.UVGC_174_48})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_506_810,(0,1,2):C.UVGC_506_811,(0,2,0):C.UVGC_507_812,(0,2,2):C.UVGC_507_813})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_515_818,(0,1,2):C.UVGC_515_819,(0,2,0):C.UVGC_516_820,(0,2,2):C.UVGC_516_821})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_524_825,(0,1,2):C.UVGC_524_826,(0,2,0):C.UVGC_525_827,(0,2,2):C.UVGC_525_828})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_506_810,(0,1,2):C.UVGC_506_811,(0,2,0):C.UVGC_507_812,(0,2,2):C.UVGC_507_813})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_515_818,(0,1,2):C.UVGC_515_819,(0,2,0):C.UVGC_516_820,(0,2,2):C.UVGC_516_821})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_524_825,(0,1,2):C.UVGC_524_826,(0,2,0):C.UVGC_525_827,(0,2,2):C.UVGC_525_828})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_275_377})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_557_870,(0,0,2):C.UVGC_557_871,(0,0,1):C.UVGC_557_872})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_557_870,(0,0,2):C.UVGC_557_871,(0,0,1):C.UVGC_557_872})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_277_411})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_557_870,(0,0,2):C.UVGC_557_871,(0,0,1):C.UVGC_557_872})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_557_870,(0,0,2):C.UVGC_557_871,(0,0,1):C.UVGC_557_872})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_276_378})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_278_444})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_281_481,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_281_481,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_289_521,(0,1,0):C.UVGC_288_520})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_722_978,(0,0,2):C.UVGC_722_979,(0,0,1):C.UVGC_722_980})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_722_978,(0,0,2):C.UVGC_722_979,(0,0,1):C.UVGC_722_980})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_292_524,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_291_523})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_722_978,(0,0,2):C.UVGC_722_979,(0,0,1):C.UVGC_722_980})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_722_978,(0,0,2):C.UVGC_722_979,(0,0,1):C.UVGC_722_980})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_290_522})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_293_525})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_296_526,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_296_526,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_304_534,(0,1,0):C.UVGC_303_533})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_544_835,(0,0,2):C.UVGC_544_836,(0,0,1):C.UVGC_544_837})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_544_835,(0,0,2):C.UVGC_544_836,(0,0,1):C.UVGC_544_837})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_307_537,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_306_536})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_544_835,(0,0,2):C.UVGC_544_836,(0,0,1):C.UVGC_544_837})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_544_835,(0,0,2):C.UVGC_544_836,(0,0,1):C.UVGC_544_837})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_305_535})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_308_538})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_311_539,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_311_539,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_319_547,(0,1,0):C.UVGC_318_546})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_558_873,(0,0,2):C.UVGC_558_874,(0,0,1):C.UVGC_558_875})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_558_873,(0,0,2):C.UVGC_558_874,(0,0,1):C.UVGC_558_875})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_624_903,(0,0,2):C.UVGC_624_904,(0,0,1):C.UVGC_624_905,(0,1,0):C.UVGC_623_901,(0,1,2):C.UVGC_623_902,(0,1,1):C.UVGC_552_859})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_322_550,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_321_549})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_558_873,(0,0,2):C.UVGC_558_874,(0,0,1):C.UVGC_558_875})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_558_873,(0,0,2):C.UVGC_558_874,(0,0,1):C.UVGC_558_875})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_622_899,(0,0,2):C.UVGC_622_900,(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_625_906,(0,1,2):C.UVGC_625_907,(0,1,1):C.UVGC_624_905})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_320_548})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_621_898,(0,0,2):C.UVGC_620_895,(0,0,1):C.UVGC_620_897})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_323_551})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_326_552,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_326_552,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_592,(0,1,0):C.UVGC_333_591})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_723_981,(0,0,2):C.UVGC_723_982,(0,0,1):C.UVGC_550_853})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_723_981,(0,0,2):C.UVGC_723_982,(0,0,1):C.UVGC_550_853})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_657_954,(0,0,2):C.UVGC_657_955,(0,0,1):C.UVGC_624_905,(0,1,0):C.UVGC_656_952,(0,1,2):C.UVGC_656_953,(0,1,1):C.UVGC_552_859})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_337_595,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_336_594})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_723_981,(0,0,2):C.UVGC_723_982,(0,0,1):C.UVGC_550_853})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_723_981,(0,0,2):C.UVGC_723_982,(0,0,1):C.UVGC_550_853})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_655_950,(0,0,2):C.UVGC_655_951,(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_658_956,(0,1,2):C.UVGC_658_957,(0,1,1):C.UVGC_624_905})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_593})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_654_949,(0,0,2):C.UVGC_620_895,(0,0,1):C.UVGC_620_897})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_338_596})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_341_597,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_341_597,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_349_605,(0,1,0):C.UVGC_348_604})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_545_838,(0,0,2):C.UVGC_545_839,(0,0,1):C.UVGC_545_840})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_545_838,(0,0,2):C.UVGC_545_839,(0,0,1):C.UVGC_545_840})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_688_970,(0,0,2):C.UVGC_688_971,(0,0,1):C.UVGC_624_905,(0,1,0):C.UVGC_687_968,(0,1,2):C.UVGC_687_969,(0,1,1):C.UVGC_552_859})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_352_608,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_351_607})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_545_838,(0,0,2):C.UVGC_545_839,(0,0,1):C.UVGC_545_840})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_545_838,(0,0,2):C.UVGC_545_839,(0,0,1):C.UVGC_545_840})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_686_966,(0,0,2):C.UVGC_686_967,(0,0,1):C.UVGC_552_859,(0,1,0):C.UVGC_689_972,(0,1,2):C.UVGC_689_973,(0,1,1):C.UVGC_624_905})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_350_606})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_685_965,(0,0,2):C.UVGC_620_895,(0,0,1):C.UVGC_620_897})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_412,(0,0,1):C.UVGC_278_413,(0,0,2):C.UVGC_278_414,(0,0,3):C.UVGC_278_415,(0,0,4):C.UVGC_278_416,(0,0,6):C.UVGC_278_417,(0,0,7):C.UVGC_278_418,(0,0,8):C.UVGC_278_419,(0,0,9):C.UVGC_278_420,(0,0,10):C.UVGC_278_421,(0,0,11):C.UVGC_278_422,(0,0,12):C.UVGC_278_423,(0,0,13):C.UVGC_278_424,(0,0,14):C.UVGC_278_425,(0,0,15):C.UVGC_278_426,(0,0,16):C.UVGC_278_427,(0,0,17):C.UVGC_278_428,(0,0,18):C.UVGC_278_429,(0,0,19):C.UVGC_278_430,(0,0,20):C.UVGC_278_431,(0,0,21):C.UVGC_278_432,(0,0,22):C.UVGC_278_433,(0,0,23):C.UVGC_278_434,(0,0,24):C.UVGC_278_435,(0,0,25):C.UVGC_278_436,(0,0,26):C.UVGC_278_437,(0,0,27):C.UVGC_278_438,(0,0,28):C.UVGC_278_439,(0,0,29):C.UVGC_278_440,(0,0,30):C.UVGC_278_441,(0,0,31):C.UVGC_278_442,(0,0,32):C.UVGC_278_443,(0,0,5):C.UVGC_353_609})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_356_610,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_356_610,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_363_617,(0,1,0):C.UVGC_364_618})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1014,(0,0,2):C.UVGC_738_1015,(0,0,1):C.UVGC_558_875})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1014,(0,0,2):C.UVGC_738_1015,(0,0,1):C.UVGC_558_875})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_626_908,(0,0,2):C.UVGC_626_909,(0,0,1):C.UVGC_626_910})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_627_943,(0,0,7):C.UVGC_627_944,(0,0,6):C.UVGC_627_945})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_367_621,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_366_620})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1014,(0,0,2):C.UVGC_738_1015,(0,0,1):C.UVGC_558_875})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1014,(0,0,2):C.UVGC_738_1015,(0,0,1):C.UVGC_558_875})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_626_908,(0,0,2):C.UVGC_626_909,(0,0,1):C.UVGC_626_910})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_627_943,(0,0,7):C.UVGC_627_944,(0,0,6):C.UVGC_627_945})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_365_619})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_620_895,(0,0,2):C.UVGC_620_896,(0,0,1):C.UVGC_620_897})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_368_654})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_371_655,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_371_655,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_378_694})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_550_851,(0,0,2):C.UVGC_550_852,(0,0,1):C.UVGC_550_853})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_550_851,(0,0,2):C.UVGC_550_852,(0,0,1):C.UVGC_550_853})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_659_958,(0,0,2):C.UVGC_659_959,(0,0,1):C.UVGC_626_910})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_660_960,(0,0,7):C.UVGC_660_961,(0,0,6):C.UVGC_627_945})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_380_696})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_550_851,(0,0,2):C.UVGC_550_852,(0,0,1):C.UVGC_550_853})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_550_851,(0,0,2):C.UVGC_550_852,(0,0,1):C.UVGC_550_853})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_659_958,(0,0,2):C.UVGC_659_959,(0,0,1):C.UVGC_626_910})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_660_960,(0,0,7):C.UVGC_660_961,(0,0,6):C.UVGC_627_945})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_379_695})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_620_895,(0,0,2):C.UVGC_653_948,(0,0,1):C.UVGC_620_897})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_381_697})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_384_698,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_384_698,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_391_705})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_731_999,(0,0,2):C.UVGC_731_1000,(0,0,1):C.UVGC_545_840})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_731_999,(0,0,2):C.UVGC_731_1000,(0,0,1):C.UVGC_545_840})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_690_974,(0,0,2):C.UVGC_690_975,(0,0,1):C.UVGC_626_910})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_691_976,(0,0,7):C.UVGC_691_977,(0,0,6):C.UVGC_627_945})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_393_707})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_731_999,(0,0,2):C.UVGC_731_1000,(0,0,1):C.UVGC_545_840})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_731_999,(0,0,2):C.UVGC_731_1000,(0,0,1):C.UVGC_545_840})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_690_974,(0,0,2):C.UVGC_690_975,(0,0,1):C.UVGC_626_910})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_627_911,(0,0,1):C.UVGC_627_912,(0,0,2):C.UVGC_627_913,(0,0,3):C.UVGC_627_914,(0,0,4):C.UVGC_627_915,(0,0,8):C.UVGC_627_916,(0,0,9):C.UVGC_627_917,(0,0,10):C.UVGC_627_918,(0,0,11):C.UVGC_627_919,(0,0,12):C.UVGC_627_920,(0,0,13):C.UVGC_627_921,(0,0,14):C.UVGC_627_922,(0,0,15):C.UVGC_627_923,(0,0,16):C.UVGC_627_924,(0,0,17):C.UVGC_627_925,(0,0,18):C.UVGC_627_926,(0,0,19):C.UVGC_627_927,(0,0,20):C.UVGC_627_928,(0,0,21):C.UVGC_627_929,(0,0,22):C.UVGC_627_930,(0,0,23):C.UVGC_627_931,(0,0,24):C.UVGC_627_932,(0,0,25):C.UVGC_627_933,(0,0,26):C.UVGC_627_934,(0,0,27):C.UVGC_627_935,(0,0,28):C.UVGC_627_936,(0,0,29):C.UVGC_627_937,(0,0,30):C.UVGC_627_938,(0,0,31):C.UVGC_627_939,(0,0,32):C.UVGC_627_940,(0,0,33):C.UVGC_627_941,(0,0,34):C.UVGC_627_942,(0,0,5):C.UVGC_691_976,(0,0,7):C.UVGC_691_977,(0,0,6):C.UVGC_627_945})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_392_706})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_620_895,(0,0,2):C.UVGC_684_964,(0,0,1):C.UVGC_620_897})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_394_708})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_397_709,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_397_709,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_404_716})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1016,(0,0,2):C.UVGC_739_1017,(0,0,1):C.UVGC_739_1018})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1016,(0,0,2):C.UVGC_739_1017,(0,0,1):C.UVGC_739_1018})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_406_718})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1016,(0,0,2):C.UVGC_739_1017,(0,0,1):C.UVGC_739_1018})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1016,(0,0,2):C.UVGC_739_1017,(0,0,1):C.UVGC_739_1018})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_405_717})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_407_719})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_410_720,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_410_720,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_417_759})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_551_854,(0,0,2):C.UVGC_551_855,(0,0,1):C.UVGC_551_856})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_551_854,(0,0,2):C.UVGC_551_855,(0,0,1):C.UVGC_551_856})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_419_761})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_551_854,(0,0,2):C.UVGC_551_855,(0,0,1):C.UVGC_551_856})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_551_854,(0,0,2):C.UVGC_551_855,(0,0,1):C.UVGC_551_856})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_418_760})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_420_762})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_423_763,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_423_763,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_430_770})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_732_1001,(0,0,2):C.UVGC_732_1002,(0,0,1):C.UVGC_732_1003})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_732_1001,(0,0,2):C.UVGC_732_1002,(0,0,1):C.UVGC_732_1003})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_277_379,(0,0,1):C.UVGC_277_380,(0,0,2):C.UVGC_277_381,(0,0,3):C.UVGC_277_382,(0,0,4):C.UVGC_277_383,(0,0,6):C.UVGC_277_384,(0,0,7):C.UVGC_277_385,(0,0,8):C.UVGC_277_386,(0,0,9):C.UVGC_277_387,(0,0,10):C.UVGC_277_388,(0,0,11):C.UVGC_277_389,(0,0,12):C.UVGC_277_390,(0,0,13):C.UVGC_277_391,(0,0,14):C.UVGC_277_392,(0,0,15):C.UVGC_277_393,(0,0,16):C.UVGC_277_394,(0,0,17):C.UVGC_277_395,(0,0,18):C.UVGC_277_396,(0,0,19):C.UVGC_277_397,(0,0,20):C.UVGC_277_398,(0,0,21):C.UVGC_277_399,(0,0,22):C.UVGC_277_400,(0,0,23):C.UVGC_277_401,(0,0,24):C.UVGC_277_402,(0,0,25):C.UVGC_277_403,(0,0,26):C.UVGC_277_404,(0,0,27):C.UVGC_277_405,(0,0,28):C.UVGC_277_406,(0,0,29):C.UVGC_277_407,(0,0,30):C.UVGC_277_408,(0,0,31):C.UVGC_277_409,(0,0,32):C.UVGC_277_410,(0,0,5):C.UVGC_432_772})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_732_1001,(0,0,2):C.UVGC_732_1002,(0,0,1):C.UVGC_732_1003})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_732_1001,(0,0,2):C.UVGC_732_1002,(0,0,1):C.UVGC_732_1003})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_431_771})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_622,(0,0,1):C.UVGC_368_623,(0,0,2):C.UVGC_368_624,(0,0,3):C.UVGC_368_625,(0,0,4):C.UVGC_368_626,(0,0,6):C.UVGC_368_627,(0,0,7):C.UVGC_368_628,(0,0,8):C.UVGC_368_629,(0,0,9):C.UVGC_368_630,(0,0,10):C.UVGC_368_631,(0,0,11):C.UVGC_368_632,(0,0,12):C.UVGC_368_633,(0,0,13):C.UVGC_368_634,(0,0,14):C.UVGC_368_635,(0,0,15):C.UVGC_368_636,(0,0,16):C.UVGC_368_637,(0,0,17):C.UVGC_368_638,(0,0,18):C.UVGC_368_639,(0,0,19):C.UVGC_368_640,(0,0,20):C.UVGC_368_641,(0,0,21):C.UVGC_368_642,(0,0,22):C.UVGC_368_643,(0,0,23):C.UVGC_368_644,(0,0,24):C.UVGC_368_645,(0,0,25):C.UVGC_368_646,(0,0,26):C.UVGC_368_647,(0,0,27):C.UVGC_368_648,(0,0,28):C.UVGC_368_649,(0,0,29):C.UVGC_368_650,(0,0,30):C.UVGC_368_651,(0,0,31):C.UVGC_368_652,(0,0,32):C.UVGC_368_653,(0,0,5):C.UVGC_433_773})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_281_449,(2,0,1):C.UVGC_281_450,(2,0,2):C.UVGC_281_451,(2,0,3):C.UVGC_281_452,(2,0,4):C.UVGC_281_453,(2,0,6):C.UVGC_281_454,(2,0,7):C.UVGC_281_455,(2,0,8):C.UVGC_281_456,(2,0,9):C.UVGC_281_457,(2,0,10):C.UVGC_281_458,(2,0,11):C.UVGC_281_459,(2,0,12):C.UVGC_281_460,(2,0,13):C.UVGC_281_461,(2,0,14):C.UVGC_281_462,(2,0,15):C.UVGC_281_463,(2,0,16):C.UVGC_281_464,(2,0,17):C.UVGC_281_465,(2,0,18):C.UVGC_281_466,(2,0,19):C.UVGC_281_467,(2,0,20):C.UVGC_281_468,(2,0,21):C.UVGC_281_469,(2,0,22):C.UVGC_281_470,(2,0,23):C.UVGC_281_471,(2,0,24):C.UVGC_281_472,(2,0,25):C.UVGC_281_473,(2,0,26):C.UVGC_281_474,(2,0,27):C.UVGC_281_475,(2,0,28):C.UVGC_281_476,(2,0,29):C.UVGC_281_477,(2,0,30):C.UVGC_281_478,(2,0,31):C.UVGC_281_479,(2,0,32):C.UVGC_281_480,(2,0,5):C.UVGC_436_774,(1,0,0):C.UVGC_281_449,(1,0,1):C.UVGC_281_450,(1,0,2):C.UVGC_281_451,(1,0,3):C.UVGC_281_452,(1,0,4):C.UVGC_281_453,(1,0,6):C.UVGC_281_454,(1,0,7):C.UVGC_281_455,(1,0,8):C.UVGC_281_456,(1,0,9):C.UVGC_281_457,(1,0,10):C.UVGC_281_458,(1,0,11):C.UVGC_281_459,(1,0,12):C.UVGC_281_460,(1,0,13):C.UVGC_281_461,(1,0,14):C.UVGC_281_462,(1,0,15):C.UVGC_281_463,(1,0,16):C.UVGC_281_464,(1,0,17):C.UVGC_281_465,(1,0,18):C.UVGC_281_466,(1,0,19):C.UVGC_281_467,(1,0,20):C.UVGC_281_468,(1,0,21):C.UVGC_281_469,(1,0,22):C.UVGC_281_470,(1,0,23):C.UVGC_281_471,(1,0,24):C.UVGC_281_472,(1,0,25):C.UVGC_281_473,(1,0,26):C.UVGC_281_474,(1,0,27):C.UVGC_281_475,(1,0,28):C.UVGC_281_476,(1,0,29):C.UVGC_281_477,(1,0,30):C.UVGC_281_478,(1,0,31):C.UVGC_281_479,(1,0,32):C.UVGC_281_480,(1,0,5):C.UVGC_436_774,(0,0,3):C.UVGC_280_447,(0,0,5):C.UVGC_280_448})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_730_996,(0,0,2):C.UVGC_730_997,(0,0,1):C.UVGC_730_998})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_487_802,(0,1,0):C.UVGC_485_800,(0,2,0):C.UVGC_486_801})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_487_802,(0,1,0):C.UVGC_492_804,(0,2,0):C.UVGC_493_805})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_487_802,(0,1,0):C.UVGC_499_807,(0,2,0):C.UVGC_500_808})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_510_816,(0,1,0):C.UVGC_508_814,(0,2,0):C.UVGC_509_815})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_510_816,(0,1,0):C.UVGC_517_822,(0,2,0):C.UVGC_518_823})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_510_816,(0,1,0):C.UVGC_526_829,(0,2,0):C.UVGC_527_830})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_470_796,(0,1,0):C.UVGC_159_33,(0,2,0):C.UVGC_160_34})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_470_796,(0,1,0):C.UVGC_167_41,(0,2,0):C.UVGC_168_42})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_470_796,(0,1,0):C.UVGC_175_49,(0,2,0):C.UVGC_176_50})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_533_832,(0,1,0):C.UVGC_219_93,(0,2,0):C.UVGC_220_94})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_533_832,(0,1,0):C.UVGC_227_101,(0,2,0):C.UVGC_228_102})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_533_832,(0,1,0):C.UVGC_235_109,(0,2,0):C.UVGC_236_110})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_283_483})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_284_484})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_285_485,(0,0,1):C.UVGC_285_486,(0,0,2):C.UVGC_285_487,(0,0,3):C.UVGC_285_488,(0,0,4):C.UVGC_285_489,(0,0,6):C.UVGC_285_490,(0,0,7):C.UVGC_285_491,(0,0,8):C.UVGC_285_492,(0,0,9):C.UVGC_285_493,(0,0,10):C.UVGC_285_494,(0,0,11):C.UVGC_285_495,(0,0,12):C.UVGC_285_496,(0,0,13):C.UVGC_285_497,(0,0,14):C.UVGC_285_498,(0,0,15):C.UVGC_285_499,(0,0,16):C.UVGC_285_500,(0,0,17):C.UVGC_285_501,(0,0,18):C.UVGC_285_502,(0,0,19):C.UVGC_285_503,(0,0,20):C.UVGC_285_504,(0,0,21):C.UVGC_285_505,(0,0,22):C.UVGC_285_506,(0,0,23):C.UVGC_285_507,(0,0,24):C.UVGC_285_508,(0,0,25):C.UVGC_285_509,(0,0,26):C.UVGC_285_510,(0,0,27):C.UVGC_285_511,(0,0,28):C.UVGC_285_512,(0,0,29):C.UVGC_285_513,(0,0,30):C.UVGC_285_514,(0,0,31):C.UVGC_285_515,(0,0,32):C.UVGC_285_516,(0,0,5):C.UVGC_285_517})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_298_528})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_299_529})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_285_485,(0,0,1):C.UVGC_285_486,(0,0,2):C.UVGC_285_487,(0,0,3):C.UVGC_285_488,(0,0,4):C.UVGC_285_489,(0,0,6):C.UVGC_285_490,(0,0,7):C.UVGC_285_491,(0,0,8):C.UVGC_285_492,(0,0,9):C.UVGC_285_493,(0,0,10):C.UVGC_285_494,(0,0,11):C.UVGC_285_495,(0,0,12):C.UVGC_285_496,(0,0,13):C.UVGC_285_497,(0,0,14):C.UVGC_285_498,(0,0,15):C.UVGC_285_499,(0,0,16):C.UVGC_285_500,(0,0,17):C.UVGC_285_501,(0,0,18):C.UVGC_285_502,(0,0,19):C.UVGC_285_503,(0,0,20):C.UVGC_285_504,(0,0,21):C.UVGC_285_505,(0,0,22):C.UVGC_285_506,(0,0,23):C.UVGC_285_507,(0,0,24):C.UVGC_285_508,(0,0,25):C.UVGC_285_509,(0,0,26):C.UVGC_285_510,(0,0,27):C.UVGC_285_511,(0,0,28):C.UVGC_285_512,(0,0,29):C.UVGC_285_513,(0,0,30):C.UVGC_285_514,(0,0,31):C.UVGC_285_515,(0,0,32):C.UVGC_285_516,(0,0,5):C.UVGC_300_530})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_313_541})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_314_542})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_285_485,(0,0,1):C.UVGC_285_486,(0,0,2):C.UVGC_285_487,(0,0,3):C.UVGC_285_488,(0,0,4):C.UVGC_285_489,(0,0,6):C.UVGC_285_490,(0,0,7):C.UVGC_285_491,(0,0,8):C.UVGC_285_492,(0,0,9):C.UVGC_285_493,(0,0,10):C.UVGC_285_494,(0,0,11):C.UVGC_285_495,(0,0,12):C.UVGC_285_496,(0,0,13):C.UVGC_285_497,(0,0,14):C.UVGC_285_498,(0,0,15):C.UVGC_285_499,(0,0,16):C.UVGC_285_500,(0,0,17):C.UVGC_285_501,(0,0,18):C.UVGC_285_502,(0,0,19):C.UVGC_285_503,(0,0,20):C.UVGC_285_504,(0,0,21):C.UVGC_285_505,(0,0,22):C.UVGC_285_506,(0,0,23):C.UVGC_285_507,(0,0,24):C.UVGC_285_508,(0,0,25):C.UVGC_285_509,(0,0,26):C.UVGC_285_510,(0,0,27):C.UVGC_285_511,(0,0,28):C.UVGC_285_512,(0,0,29):C.UVGC_285_513,(0,0,30):C.UVGC_285_514,(0,0,31):C.UVGC_285_515,(0,0,32):C.UVGC_285_516,(0,0,5):C.UVGC_315_543})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_328_554})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_329_555})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_330_556,(0,0,1):C.UVGC_330_557,(0,0,2):C.UVGC_330_558,(0,0,3):C.UVGC_330_559,(0,0,4):C.UVGC_330_560,(0,0,6):C.UVGC_330_561,(0,0,7):C.UVGC_330_562,(0,0,8):C.UVGC_330_563,(0,0,9):C.UVGC_330_564,(0,0,10):C.UVGC_330_565,(0,0,11):C.UVGC_330_566,(0,0,12):C.UVGC_330_567,(0,0,13):C.UVGC_330_568,(0,0,14):C.UVGC_330_569,(0,0,15):C.UVGC_330_570,(0,0,16):C.UVGC_330_571,(0,0,17):C.UVGC_330_572,(0,0,18):C.UVGC_330_573,(0,0,19):C.UVGC_330_574,(0,0,20):C.UVGC_330_575,(0,0,21):C.UVGC_330_576,(0,0,22):C.UVGC_330_577,(0,0,23):C.UVGC_330_578,(0,0,24):C.UVGC_330_579,(0,0,25):C.UVGC_330_580,(0,0,26):C.UVGC_330_581,(0,0,27):C.UVGC_330_582,(0,0,28):C.UVGC_330_583,(0,0,29):C.UVGC_330_584,(0,0,30):C.UVGC_330_585,(0,0,31):C.UVGC_330_586,(0,0,32):C.UVGC_330_587,(0,0,5):C.UVGC_330_588})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_343_599})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_344_600})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_330_556,(0,0,1):C.UVGC_330_557,(0,0,2):C.UVGC_330_558,(0,0,3):C.UVGC_330_559,(0,0,4):C.UVGC_330_560,(0,0,6):C.UVGC_330_561,(0,0,7):C.UVGC_330_562,(0,0,8):C.UVGC_330_563,(0,0,9):C.UVGC_330_564,(0,0,10):C.UVGC_330_565,(0,0,11):C.UVGC_330_566,(0,0,12):C.UVGC_330_567,(0,0,13):C.UVGC_330_568,(0,0,14):C.UVGC_330_569,(0,0,15):C.UVGC_330_570,(0,0,16):C.UVGC_330_571,(0,0,17):C.UVGC_330_572,(0,0,18):C.UVGC_330_573,(0,0,19):C.UVGC_330_574,(0,0,20):C.UVGC_330_575,(0,0,21):C.UVGC_330_576,(0,0,22):C.UVGC_330_577,(0,0,23):C.UVGC_330_578,(0,0,24):C.UVGC_330_579,(0,0,25):C.UVGC_330_580,(0,0,26):C.UVGC_330_581,(0,0,27):C.UVGC_330_582,(0,0,28):C.UVGC_330_583,(0,0,29):C.UVGC_330_584,(0,0,30):C.UVGC_330_585,(0,0,31):C.UVGC_330_586,(0,0,32):C.UVGC_330_587,(0,0,5):C.UVGC_345_601})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_358_612})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_359_613})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_330_556,(0,0,1):C.UVGC_330_557,(0,0,2):C.UVGC_330_558,(0,0,3):C.UVGC_330_559,(0,0,4):C.UVGC_330_560,(0,0,6):C.UVGC_330_561,(0,0,7):C.UVGC_330_562,(0,0,8):C.UVGC_330_563,(0,0,9):C.UVGC_330_564,(0,0,10):C.UVGC_330_565,(0,0,11):C.UVGC_330_566,(0,0,12):C.UVGC_330_567,(0,0,13):C.UVGC_330_568,(0,0,14):C.UVGC_330_569,(0,0,15):C.UVGC_330_570,(0,0,16):C.UVGC_330_571,(0,0,17):C.UVGC_330_572,(0,0,18):C.UVGC_330_573,(0,0,19):C.UVGC_330_574,(0,0,20):C.UVGC_330_575,(0,0,21):C.UVGC_330_576,(0,0,22):C.UVGC_330_577,(0,0,23):C.UVGC_330_578,(0,0,24):C.UVGC_330_579,(0,0,25):C.UVGC_330_580,(0,0,26):C.UVGC_330_581,(0,0,27):C.UVGC_330_582,(0,0,28):C.UVGC_330_583,(0,0,29):C.UVGC_330_584,(0,0,30):C.UVGC_330_585,(0,0,31):C.UVGC_330_586,(0,0,32):C.UVGC_330_587,(0,0,5):C.UVGC_360_614})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_373_657})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_617_892,(0,0,2):C.UVGC_617_893,(0,0,1):C.UVGC_617_894})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_617_892,(0,0,2):C.UVGC_617_893,(0,0,1):C.UVGC_617_894})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_374_658})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_375_659,(0,0,1):C.UVGC_375_660,(0,0,2):C.UVGC_375_661,(0,0,3):C.UVGC_375_662,(0,0,4):C.UVGC_375_663,(0,0,6):C.UVGC_375_664,(0,0,7):C.UVGC_375_665,(0,0,8):C.UVGC_375_666,(0,0,9):C.UVGC_375_667,(0,0,10):C.UVGC_375_668,(0,0,11):C.UVGC_375_669,(0,0,12):C.UVGC_375_670,(0,0,13):C.UVGC_375_671,(0,0,14):C.UVGC_375_672,(0,0,15):C.UVGC_375_673,(0,0,16):C.UVGC_375_674,(0,0,17):C.UVGC_375_675,(0,0,18):C.UVGC_375_676,(0,0,19):C.UVGC_375_677,(0,0,20):C.UVGC_375_678,(0,0,21):C.UVGC_375_679,(0,0,22):C.UVGC_375_680,(0,0,23):C.UVGC_375_681,(0,0,24):C.UVGC_375_682,(0,0,25):C.UVGC_375_683,(0,0,26):C.UVGC_375_684,(0,0,27):C.UVGC_375_685,(0,0,28):C.UVGC_375_686,(0,0,29):C.UVGC_375_687,(0,0,30):C.UVGC_375_688,(0,0,31):C.UVGC_375_689,(0,0,32):C.UVGC_375_690,(0,0,5):C.UVGC_375_691})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_386_700})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_650_946,(0,0,2):C.UVGC_650_947,(0,0,1):C.UVGC_617_894})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_650_946,(0,0,2):C.UVGC_650_947,(0,0,1):C.UVGC_617_894})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_387_701})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_375_659,(0,0,1):C.UVGC_375_660,(0,0,2):C.UVGC_375_661,(0,0,3):C.UVGC_375_662,(0,0,4):C.UVGC_375_663,(0,0,6):C.UVGC_375_664,(0,0,7):C.UVGC_375_665,(0,0,8):C.UVGC_375_666,(0,0,9):C.UVGC_375_667,(0,0,10):C.UVGC_375_668,(0,0,11):C.UVGC_375_669,(0,0,12):C.UVGC_375_670,(0,0,13):C.UVGC_375_671,(0,0,14):C.UVGC_375_672,(0,0,15):C.UVGC_375_673,(0,0,16):C.UVGC_375_674,(0,0,17):C.UVGC_375_675,(0,0,18):C.UVGC_375_676,(0,0,19):C.UVGC_375_677,(0,0,20):C.UVGC_375_678,(0,0,21):C.UVGC_375_679,(0,0,22):C.UVGC_375_680,(0,0,23):C.UVGC_375_681,(0,0,24):C.UVGC_375_682,(0,0,25):C.UVGC_375_683,(0,0,26):C.UVGC_375_684,(0,0,27):C.UVGC_375_685,(0,0,28):C.UVGC_375_686,(0,0,29):C.UVGC_375_687,(0,0,30):C.UVGC_375_688,(0,0,31):C.UVGC_375_689,(0,0,32):C.UVGC_375_690,(0,0,5):C.UVGC_388_702})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_399_711})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_681_962,(0,0,2):C.UVGC_681_963,(0,0,1):C.UVGC_617_894})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_681_962,(0,0,2):C.UVGC_681_963,(0,0,1):C.UVGC_617_894})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_400_712})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_375_659,(0,0,1):C.UVGC_375_660,(0,0,2):C.UVGC_375_661,(0,0,3):C.UVGC_375_662,(0,0,4):C.UVGC_375_663,(0,0,6):C.UVGC_375_664,(0,0,7):C.UVGC_375_665,(0,0,8):C.UVGC_375_666,(0,0,9):C.UVGC_375_667,(0,0,10):C.UVGC_375_668,(0,0,11):C.UVGC_375_669,(0,0,12):C.UVGC_375_670,(0,0,13):C.UVGC_375_671,(0,0,14):C.UVGC_375_672,(0,0,15):C.UVGC_375_673,(0,0,16):C.UVGC_375_674,(0,0,17):C.UVGC_375_675,(0,0,18):C.UVGC_375_676,(0,0,19):C.UVGC_375_677,(0,0,20):C.UVGC_375_678,(0,0,21):C.UVGC_375_679,(0,0,22):C.UVGC_375_680,(0,0,23):C.UVGC_375_681,(0,0,24):C.UVGC_375_682,(0,0,25):C.UVGC_375_683,(0,0,26):C.UVGC_375_684,(0,0,27):C.UVGC_375_685,(0,0,28):C.UVGC_375_686,(0,0,29):C.UVGC_375_687,(0,0,30):C.UVGC_375_688,(0,0,31):C.UVGC_375_689,(0,0,32):C.UVGC_375_690,(0,0,5):C.UVGC_401_713})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_412_722})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_413_723})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_414_724,(0,0,1):C.UVGC_414_725,(0,0,2):C.UVGC_414_726,(0,0,3):C.UVGC_414_727,(0,0,4):C.UVGC_414_728,(0,0,6):C.UVGC_414_729,(0,0,7):C.UVGC_414_730,(0,0,8):C.UVGC_414_731,(0,0,9):C.UVGC_414_732,(0,0,10):C.UVGC_414_733,(0,0,11):C.UVGC_414_734,(0,0,12):C.UVGC_414_735,(0,0,13):C.UVGC_414_736,(0,0,14):C.UVGC_414_737,(0,0,15):C.UVGC_414_738,(0,0,16):C.UVGC_414_739,(0,0,17):C.UVGC_414_740,(0,0,18):C.UVGC_414_741,(0,0,19):C.UVGC_414_742,(0,0,20):C.UVGC_414_743,(0,0,21):C.UVGC_414_744,(0,0,22):C.UVGC_414_745,(0,0,23):C.UVGC_414_746,(0,0,24):C.UVGC_414_747,(0,0,25):C.UVGC_414_748,(0,0,26):C.UVGC_414_749,(0,0,27):C.UVGC_414_750,(0,0,28):C.UVGC_414_751,(0,0,29):C.UVGC_414_752,(0,0,30):C.UVGC_414_753,(0,0,31):C.UVGC_414_754,(0,0,32):C.UVGC_414_755,(0,0,5):C.UVGC_414_756})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_425_765})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_426_766})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_414_724,(0,0,1):C.UVGC_414_725,(0,0,2):C.UVGC_414_726,(0,0,3):C.UVGC_414_727,(0,0,4):C.UVGC_414_728,(0,0,6):C.UVGC_414_729,(0,0,7):C.UVGC_414_730,(0,0,8):C.UVGC_414_731,(0,0,9):C.UVGC_414_732,(0,0,10):C.UVGC_414_733,(0,0,11):C.UVGC_414_734,(0,0,12):C.UVGC_414_735,(0,0,13):C.UVGC_414_736,(0,0,14):C.UVGC_414_737,(0,0,15):C.UVGC_414_738,(0,0,16):C.UVGC_414_739,(0,0,17):C.UVGC_414_740,(0,0,18):C.UVGC_414_741,(0,0,19):C.UVGC_414_742,(0,0,20):C.UVGC_414_743,(0,0,21):C.UVGC_414_744,(0,0,22):C.UVGC_414_745,(0,0,23):C.UVGC_414_746,(0,0,24):C.UVGC_414_747,(0,0,25):C.UVGC_414_748,(0,0,26):C.UVGC_414_749,(0,0,27):C.UVGC_414_750,(0,0,28):C.UVGC_414_751,(0,0,29):C.UVGC_414_752,(0,0,30):C.UVGC_414_753,(0,0,31):C.UVGC_414_754,(0,0,32):C.UVGC_414_755,(0,0,5):C.UVGC_427_767})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_438_776})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_439_777})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_414_724,(0,0,1):C.UVGC_414_725,(0,0,2):C.UVGC_414_726,(0,0,3):C.UVGC_414_727,(0,0,4):C.UVGC_414_728,(0,0,6):C.UVGC_414_729,(0,0,7):C.UVGC_414_730,(0,0,8):C.UVGC_414_731,(0,0,9):C.UVGC_414_732,(0,0,10):C.UVGC_414_733,(0,0,11):C.UVGC_414_734,(0,0,12):C.UVGC_414_735,(0,0,13):C.UVGC_414_736,(0,0,14):C.UVGC_414_737,(0,0,15):C.UVGC_414_738,(0,0,16):C.UVGC_414_739,(0,0,17):C.UVGC_414_740,(0,0,18):C.UVGC_414_741,(0,0,19):C.UVGC_414_742,(0,0,20):C.UVGC_414_743,(0,0,21):C.UVGC_414_744,(0,0,22):C.UVGC_414_745,(0,0,23):C.UVGC_414_746,(0,0,24):C.UVGC_414_747,(0,0,25):C.UVGC_414_748,(0,0,26):C.UVGC_414_749,(0,0,27):C.UVGC_414_750,(0,0,28):C.UVGC_414_751,(0,0,29):C.UVGC_414_752,(0,0,30):C.UVGC_414_753,(0,0,31):C.UVGC_414_754,(0,0,32):C.UVGC_414_755,(0,0,5):C.UVGC_440_778})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_286_518})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_301_531})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_316_544})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_331_589})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_346_602})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_361_615})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_376_692})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_389_703})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_402_714})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_415_757})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_428_768})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_441_779})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_740_1020,(0,0,1):C.UVGC_561_883})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_561_882,(0,0,1):C.UVGC_561_883})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_553_861,(0,0,1):C.UVGC_553_862})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_726_989,(0,0,1):C.UVGC_553_862})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_733_1005,(0,0,1):C.UVGC_548_848})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_548_847,(0,0,1):C.UVGC_548_848})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_740_1020,(0,0,1):C.UVGC_561_883})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_561_882,(0,0,1):C.UVGC_561_883})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_553_861,(0,0,1):C.UVGC_553_862})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_726_989,(0,0,1):C.UVGC_553_862})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_733_1005,(0,0,1):C.UVGC_548_848})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_548_847,(0,0,1):C.UVGC_548_848})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_150_24,(0,2,0):C.UVGC_152_26})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_134_8,(0,2,0):C.UVGC_136_10})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_263_369,(0,1,0):C.UVGC_146_20,(0,2,0):C.UVGC_148_22})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_138_12,(0,2,0):C.UVGC_140_14})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_142_16,(0,2,0):C.UVGC_144_18})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_256_363,(0,1,0):C.UVGC_130_4,(0,2,0):C.UVGC_132_6})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_459_791,(0,2,0):C.UVGC_242_119,(0,2,1):C.UVGC_242_120,(0,2,2):C.UVGC_242_121,(0,2,3):C.UVGC_242_122,(0,2,4):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,5):C.UVGC_460_792})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,3):C.UVGC_242_121,(0,1,4):C.UVGC_242_122,(0,1,5):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,2):C.UVGC_260_367,(0,2,0):C.UVGC_242_119,(0,2,1):C.UVGC_242_120,(0,2,3):C.UVGC_242_121,(0,2,4):C.UVGC_242_122,(0,2,5):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,2):C.UVGC_261_368})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_449_784,(0,2,0):C.UVGC_242_119,(0,2,1):C.UVGC_242_120,(0,2,2):C.UVGC_242_121,(0,2,3):C.UVGC_242_122,(0,2,4):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,5):C.UVGC_450_785})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,4):C.UVGC_242_122,(0,1,5):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,3):C.UVGC_267_372,(0,2,0):C.UVGC_242_119,(0,2,1):C.UVGC_242_120,(0,2,2):C.UVGC_242_121,(0,2,4):C.UVGC_242_122,(0,2,5):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,3):C.UVGC_268_373})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,1):C.UVGC_242_120,(0,1,2):C.UVGC_242_121,(0,1,3):C.UVGC_242_122,(0,1,4):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,5):C.UVGC_442_780,(0,2,0):C.UVGC_242_119,(0,2,1):C.UVGC_242_120,(0,2,2):C.UVGC_242_121,(0,2,3):C.UVGC_242_122,(0,2,4):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,5):C.UVGC_443_781})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_257_364,(0,1,0):C.UVGC_242_119,(0,1,2):C.UVGC_242_120,(0,1,3):C.UVGC_242_121,(0,1,4):C.UVGC_242_122,(0,1,5):C.UVGC_242_123,(0,1,6):C.UVGC_242_124,(0,1,7):C.UVGC_242_125,(0,1,8):C.UVGC_242_126,(0,1,9):C.UVGC_242_127,(0,1,10):C.UVGC_242_128,(0,1,11):C.UVGC_242_129,(0,1,12):C.UVGC_242_130,(0,1,13):C.UVGC_242_131,(0,1,14):C.UVGC_242_132,(0,1,15):C.UVGC_242_133,(0,1,16):C.UVGC_242_134,(0,1,17):C.UVGC_242_135,(0,1,18):C.UVGC_242_136,(0,1,19):C.UVGC_242_137,(0,1,20):C.UVGC_242_138,(0,1,21):C.UVGC_242_139,(0,1,22):C.UVGC_242_140,(0,1,23):C.UVGC_242_141,(0,1,24):C.UVGC_242_142,(0,1,25):C.UVGC_242_143,(0,1,26):C.UVGC_242_144,(0,1,27):C.UVGC_242_145,(0,1,28):C.UVGC_242_146,(0,1,29):C.UVGC_242_147,(0,1,30):C.UVGC_242_148,(0,1,31):C.UVGC_242_149,(0,1,32):C.UVGC_242_150,(0,1,1):C.UVGC_253_360,(0,2,0):C.UVGC_242_119,(0,2,2):C.UVGC_242_120,(0,2,3):C.UVGC_242_121,(0,2,4):C.UVGC_242_122,(0,2,5):C.UVGC_242_123,(0,2,6):C.UVGC_242_124,(0,2,7):C.UVGC_242_125,(0,2,8):C.UVGC_242_126,(0,2,9):C.UVGC_242_127,(0,2,10):C.UVGC_242_128,(0,2,11):C.UVGC_242_129,(0,2,12):C.UVGC_242_130,(0,2,13):C.UVGC_242_131,(0,2,14):C.UVGC_242_132,(0,2,15):C.UVGC_242_133,(0,2,16):C.UVGC_242_134,(0,2,17):C.UVGC_242_135,(0,2,18):C.UVGC_242_136,(0,2,19):C.UVGC_242_137,(0,2,20):C.UVGC_242_138,(0,2,21):C.UVGC_242_139,(0,2,22):C.UVGC_242_140,(0,2,23):C.UVGC_242_141,(0,2,24):C.UVGC_242_142,(0,2,25):C.UVGC_242_143,(0,2,26):C.UVGC_242_144,(0,2,27):C.UVGC_242_145,(0,2,28):C.UVGC_242_146,(0,2,29):C.UVGC_242_147,(0,2,30):C.UVGC_242_148,(0,2,31):C.UVGC_242_149,(0,2,32):C.UVGC_242_150,(0,2,1):C.UVGC_254_361})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_737_1012,(0,0,2):C.UVGC_737_1013,(0,0,1):C.UVGC_552_859})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_552_857,(0,0,2):C.UVGC_552_858,(0,0,1):C.UVGC_552_859})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_728_991,(0,0,2):C.UVGC_728_992,(0,0,1):C.UVGC_552_859})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_737_1012,(0,0,2):C.UVGC_737_1013,(0,0,1):C.UVGC_552_859})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_552_857,(0,0,2):C.UVGC_552_858,(0,0,1):C.UVGC_552_859})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_728_991,(0,0,2):C.UVGC_728_992,(0,0,1):C.UVGC_552_859})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_464_793,(0,1,0):C.UVGC_465_794})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_265_370,(0,1,0):C.UVGC_266_371})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_455_787,(0,1,0):C.UVGC_456_788})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_374,(0,1,0):C.UVGC_273_375})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_447_782,(0,1,0):C.UVGC_448_783})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_258_365,(0,1,0):C.UVGC_259_366})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_740_1020,(0,0,1):C.UVGC_561_883})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_561_882,(0,0,1):C.UVGC_561_883})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_553_861,(0,0,1):C.UVGC_553_862})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_726_989,(0,0,1):C.UVGC_553_862})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_733_1005,(0,0,1):C.UVGC_548_848})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_548_847,(0,0,1):C.UVGC_548_848})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_740_1019,(0,0,2):C.UVGC_740_1020,(0,0,1):C.UVGC_561_883})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_561_881,(0,0,2):C.UVGC_561_882,(0,0,1):C.UVGC_561_883})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_553_860,(0,0,2):C.UVGC_553_861,(0,0,1):C.UVGC_553_862})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_726_988,(0,0,2):C.UVGC_726_989,(0,0,1):C.UVGC_553_862})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_733_1004,(0,0,2):C.UVGC_733_1005,(0,0,1):C.UVGC_548_848})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_548_846,(0,0,2):C.UVGC_548_847,(0,0,1):C.UVGC_548_848})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_559_877,(0,0,1):C.UVGC_559_878})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_724_984,(0,0,1):C.UVGC_724_985})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_546_842,(0,0,1):C.UVGC_546_843})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_742_1023,(0,0,1):C.UVGC_742_1024})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_555_866,(0,0,1):C.UVGC_555_867})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_735_1008,(0,0,1):C.UVGC_735_1009})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_559_877,(0,0,1):C.UVGC_559_878})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_724_984,(0,0,1):C.UVGC_724_985})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_546_842,(0,0,1):C.UVGC_546_843})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_742_1023,(0,0,1):C.UVGC_742_1024})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_555_866,(0,0,1):C.UVGC_555_867})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_735_1008,(0,0,1):C.UVGC_735_1009})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_559_877,(0,0,1):C.UVGC_559_878})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_724_984,(0,0,1):C.UVGC_724_985})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_546_842,(0,0,1):C.UVGC_546_843})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_742_1023,(0,0,1):C.UVGC_742_1024})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_555_866,(0,0,1):C.UVGC_555_867})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_735_1008,(0,0,1):C.UVGC_735_1009})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_559_876,(0,0,2):C.UVGC_559_877,(0,0,1):C.UVGC_559_878})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_724_983,(0,0,2):C.UVGC_724_984,(0,0,1):C.UVGC_724_985})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_546_841,(0,0,2):C.UVGC_546_842,(0,0,1):C.UVGC_546_843})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_742_1022,(0,0,2):C.UVGC_742_1023,(0,0,1):C.UVGC_742_1024})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_555_865,(0,0,2):C.UVGC_555_866,(0,0,1):C.UVGC_555_867})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_735_1007,(0,0,2):C.UVGC_735_1008,(0,0,1):C.UVGC_735_1009})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_255_362,(0,1,0):C.UVGC_149_23,(0,2,0):C.UVGC_151_25})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_255_362,(0,1,0):C.UVGC_133_7,(0,2,0):C.UVGC_135_9})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_454_786,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_145_19,(0,2,0):C.UVGC_147_21})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_255_362,(0,1,0):C.UVGC_137_11,(0,2,0):C.UVGC_139_13})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_255_362,(0,1,0):C.UVGC_141_15,(0,2,0):C.UVGC_143_17})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_255_362,(0,1,0):C.UVGC_129_3,(0,2,0):C.UVGC_131_5})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_505_809,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_195_69,(0,2,0):C.UVGC_197_71})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,1,0):C.UVGC_514_817,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_201_75,(0,2,0):C.UVGC_203_77})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,1,0):C.UVGC_523_824,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_207_81,(0,2,0):C.UVGC_209_83})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,1,0):C.UVGC_484_799,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_177_51,(0,2,0):C.UVGC_179_53})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,1,0):C.UVGC_491_803,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_183_57,(0,2,0):C.UVGC_185_59})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,1,0):C.UVGC_498_806,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_189_63,(0,2,0):C.UVGC_191_65})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,1,0):C.UVGC_532_831,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_213_87,(0,2,0):C.UVGC_215_89})

V_856 = CTVertex(name = 'V_856',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,1,0):C.UVGC_537_833,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_221_95,(0,2,0):C.UVGC_223_97})

V_857 = CTVertex(name = 'V_857',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,1,0):C.UVGC_542_834,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_229_103,(0,2,0):C.UVGC_231_105})

V_858 = CTVertex(name = 'V_858',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,1,0):C.UVGC_469_795,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_153_27,(0,2,0):C.UVGC_155_29})

V_859 = CTVertex(name = 'V_859',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,1,0):C.UVGC_474_797,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_161_35,(0,2,0):C.UVGC_163_37})

V_860 = CTVertex(name = 'V_860',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,1,0):C.UVGC_479_798,(0,3,0):C.UVGC_255_362,(0,0,0):C.UVGC_169_43,(0,2,0):C.UVGC_171_45})

V_861 = CTVertex(name = 'V_861',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_243_151,(0,0,1):C.UVGC_243_152,(0,0,2):C.UVGC_243_153,(0,0,3):C.UVGC_243_154,(0,0,4):C.UVGC_243_155,(0,0,5):C.UVGC_243_156,(0,0,6):C.UVGC_243_157,(0,0,7):C.UVGC_243_158,(0,0,8):C.UVGC_243_159,(0,0,9):C.UVGC_243_160,(0,0,10):C.UVGC_243_161,(0,0,11):C.UVGC_243_162,(0,0,12):C.UVGC_243_163,(0,0,13):C.UVGC_243_164,(0,0,14):C.UVGC_243_165,(0,0,15):C.UVGC_243_166,(0,0,16):C.UVGC_243_167,(0,0,17):C.UVGC_243_168,(0,0,18):C.UVGC_243_169,(0,0,19):C.UVGC_243_170,(0,0,20):C.UVGC_243_171,(0,0,21):C.UVGC_243_172,(0,0,22):C.UVGC_243_173,(0,0,23):C.UVGC_243_174,(0,0,24):C.UVGC_243_175,(0,0,25):C.UVGC_243_176,(0,0,26):C.UVGC_243_177,(0,0,27):C.UVGC_243_178,(0,0,28):C.UVGC_243_179,(0,0,29):C.UVGC_243_180,(0,0,30):C.UVGC_243_181,(0,0,31):C.UVGC_243_182,(0,1,3):C.UVGC_127_1,(0,2,4):C.UVGC_128_2})

V_862 = CTVertex(name = 'V_862',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_372_656,(0,1,0):C.UVGC_362_616})

V_863 = CTVertex(name = 'V_863',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_385_699,(0,1,0):C.UVGC_377_693})

V_864 = CTVertex(name = 'V_864',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_398_710,(0,1,0):C.UVGC_390_704})

V_865 = CTVertex(name = 'V_865',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_327_553,(0,1,0):C.UVGC_317_545})

V_866 = CTVertex(name = 'V_866',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_342_598,(0,1,0):C.UVGC_332_590})

V_867 = CTVertex(name = 'V_867',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_357_611,(0,1,0):C.UVGC_347_603})

V_868 = CTVertex(name = 'V_868',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_411_721,(0,1,0):C.UVGC_403_715})

V_869 = CTVertex(name = 'V_869',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_424_764,(0,1,0):C.UVGC_416_758})

V_870 = CTVertex(name = 'V_870',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_437_775,(0,1,0):C.UVGC_429_769})

V_871 = CTVertex(name = 'V_871',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_282_482,(0,1,0):C.UVGC_274_376})

V_872 = CTVertex(name = 'V_872',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_297_527,(0,1,0):C.UVGC_287_519})

V_873 = CTVertex(name = 'V_873',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_312_540,(0,1,0):C.UVGC_302_532})

V_874 = CTVertex(name = 'V_874',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_753_1034,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_753_1036,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_753_1034,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_753_1036})

V_875 = CTVertex(name = 'V_875',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_826_1100,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_826_1102,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_826_1103,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_825_1095,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_825_1097,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_825_1098})

V_876 = CTVertex(name = 'V_876',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_753_1034,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_753_1036,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_753_1034,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_753_1036})

V_877 = CTVertex(name = 'V_877',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_826_1100,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_826_1102,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_826_1103,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_825_1095,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_825_1097,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_825_1098})

V_878 = CTVertex(name = 'V_878',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_826_1100,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_826_1102,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_826_1103,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_825_1095,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_825_1097,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_825_1098})

V_879 = CTVertex(name = 'V_879',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_753_1034,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_753_1036,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_753_1034,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_753_1036})

V_880 = CTVertex(name = 'V_880',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,7):C.UVGC_564_890,(1,0,8):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,4):C.UVGC_759_1039,(1,0,11):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,5):C.UVGC_760_1044,(1,0,10):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1092,(1,0,9):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,7):C.UVGC_563_887,(0,0,8):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,4):C.UVGC_760_1042,(0,0,11):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,5):C.UVGC_819_1086,(0,0,10):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1088,(0,0,9):C.UVGC_819_1089})

V_881 = CTVertex(name = 'V_881',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_882 = CTVertex(name = 'V_882',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_883 = CTVertex(name = 'V_883',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_750_1031,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_750_1032,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_750_1031,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_750_1032})

V_884 = CTVertex(name = 'V_884',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_885 = CTVertex(name = 'V_885',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_886 = CTVertex(name = 'V_886',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_887 = CTVertex(name = 'V_887',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,7):C.UVGC_564_890,(1,0,8):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,4):C.UVGC_759_1039,(1,0,11):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,5):C.UVGC_760_1044,(1,0,10):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1092,(1,0,9):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,7):C.UVGC_563_887,(0,0,8):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,4):C.UVGC_760_1042,(0,0,11):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,5):C.UVGC_819_1086,(0,0,10):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1088,(0,0,9):C.UVGC_819_1089})

V_888 = CTVertex(name = 'V_888',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_889 = CTVertex(name = 'V_889',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_778_1066,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_778_1067,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_778_1068,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_777_1063,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_777_1064,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_777_1065})

V_890 = CTVertex(name = 'V_890',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_750_1031,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_750_1032,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_750_1031,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_750_1032})

V_891 = CTVertex(name = 'V_891',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_892 = CTVertex(name = 'V_892',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_893 = CTVertex(name = 'V_893',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_894 = CTVertex(name = 'V_894',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_759_1039,(1,0,1):C.UVGC_759_1040,(1,0,2):C.UVGC_759_1041,(0,0,0):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043,(0,0,2):C.UVGC_760_1044})

V_895 = CTVertex(name = 'V_895',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_896 = CTVertex(name = 'V_896',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1089})

V_897 = CTVertex(name = 'V_897',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,7):C.UVGC_564_890,(1,0,8):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,4):C.UVGC_759_1039,(1,0,11):C.UVGC_820_1090,(1,0,1):C.UVGC_782_1075,(1,0,5):C.UVGC_760_1044,(1,0,10):C.UVGC_820_1091,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_820_1092,(1,0,9):C.UVGC_820_1093,(0,0,3):C.UVGC_563_886,(0,0,7):C.UVGC_563_887,(0,0,8):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,4):C.UVGC_760_1042,(0,0,11):C.UVGC_819_1085,(0,0,1):C.UVGC_747_1029,(0,0,5):C.UVGC_819_1086,(0,0,10):C.UVGC_819_1087,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_819_1088,(0,0,9):C.UVGC_819_1089})

V_898 = CTVertex(name = 'V_898',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_778_1066,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_778_1067,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_778_1068,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_777_1063,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_777_1064,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_777_1065})

V_899 = CTVertex(name = 'V_899',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_778_1066,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_778_1067,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_778_1068,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_777_1063,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_777_1064,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_777_1065})

V_900 = CTVertex(name = 'V_900',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_750_1031,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_750_1032,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_750_1031,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_750_1032})

V_901 = CTVertex(name = 'V_901',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_902 = CTVertex(name = 'V_902',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_903 = CTVertex(name = 'V_903',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_904 = CTVertex(name = 'V_904',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_905 = CTVertex(name = 'V_905',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_906 = CTVertex(name = 'V_906',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_907 = CTVertex(name = 'V_907',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_756_1037,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_756_1038,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_756_1037,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_756_1038})

V_908 = CTVertex(name = 'V_908',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_909 = CTVertex(name = 'V_909',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_910 = CTVertex(name = 'V_910',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_911 = CTVertex(name = 'V_911',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_912 = CTVertex(name = 'V_912',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_913 = CTVertex(name = 'V_913',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_914 = CTVertex(name = 'V_914',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_880_1116,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_880_1117,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_766_1052,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_879_1114,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_879_1115,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_765_1046})

V_915 = CTVertex(name = 'V_915',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_756_1037,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_756_1038,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_756_1037,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_756_1038})

V_916 = CTVertex(name = 'V_916',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_917 = CTVertex(name = 'V_917',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_918 = CTVertex(name = 'V_918',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_830_1107,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_830_1108,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_830_1109,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_829_1104,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_829_1105,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_829_1106})

V_919 = CTVertex(name = 'V_919',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_920 = CTVertex(name = 'V_920',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_921 = CTVertex(name = 'V_921',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_782_1074,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_782_1076,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_782_1078,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_781_1069,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_781_1070,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_781_1072})

V_922 = CTVertex(name = 'V_922',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_880_1116,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_880_1117,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_766_1052,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_879_1114,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_879_1115,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_765_1046})

V_923 = CTVertex(name = 'V_923',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_826_1099,(1,0,8):C.UVGC_880_1116,(1,0,1):C.UVGC_826_1101,(1,0,7):C.UVGC_880_1117,(1,0,2):C.UVGC_766_1051,(1,0,6):C.UVGC_766_1052,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_825_1094,(0,0,8):C.UVGC_879_1114,(0,0,1):C.UVGC_825_1096,(0,0,7):C.UVGC_879_1115,(0,0,2):C.UVGC_765_1045,(0,0,6):C.UVGC_765_1046})

V_924 = CTVertex(name = 'V_924',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_753_1033,(1,0,5):C.UVGC_756_1037,(1,0,1):C.UVGC_753_1035,(1,0,4):C.UVGC_756_1038,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_753_1033,(0,0,5):C.UVGC_756_1037,(0,0,1):C.UVGC_753_1035,(0,0,4):C.UVGC_756_1038})

V_925 = CTVertex(name = 'V_925',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_926 = CTVertex(name = 'V_926',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_927 = CTVertex(name = 'V_927',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_928 = CTVertex(name = 'V_928',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_929 = CTVertex(name = 'V_929',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_930 = CTVertex(name = 'V_930',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_931 = CTVertex(name = 'V_931',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_932 = CTVertex(name = 'V_932',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_933 = CTVertex(name = 'V_933',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_934 = CTVertex(name = 'V_934',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_747_1028,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_747_1030,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_747_1030})

V_935 = CTVertex(name = 'V_935',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_936 = CTVertex(name = 'V_936',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_937 = CTVertex(name = 'V_937',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_938 = CTVertex(name = 'V_938',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_939 = CTVertex(name = 'V_939',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_940 = CTVertex(name = 'V_940',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_941 = CTVertex(name = 'V_941',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_942 = CTVertex(name = 'V_942',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_943 = CTVertex(name = 'V_943',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_944 = CTVertex(name = 'V_944',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_766_1052,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_766_1054,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_766_1056,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_765_1046,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_765_1048,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_765_1050})

V_945 = CTVertex(name = 'V_945',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_747_1028,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_747_1030,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_747_1030})

V_946 = CTVertex(name = 'V_946',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_947 = CTVertex(name = 'V_947',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_948 = CTVertex(name = 'V_948',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_814_1082,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_814_1083,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_814_1084,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_813_1079,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_813_1080,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_813_1081})

V_949 = CTVertex(name = 'V_949',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_950 = CTVertex(name = 'V_950',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_951 = CTVertex(name = 'V_951',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_772_1060,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_772_1061,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_772_1062,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_771_1057,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_771_1058,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_771_1059})

V_952 = CTVertex(name = 'V_952',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_953 = CTVertex(name = 'V_953',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_954 = CTVertex(name = 'V_954',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_782_1073,(1,0,8):C.UVGC_874_1111,(1,0,1):C.UVGC_782_1075,(1,0,7):C.UVGC_874_1112,(1,0,2):C.UVGC_782_1077,(1,0,6):C.UVGC_874_1113,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_747_1027,(0,0,8):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,7):C.UVGC_747_1030,(0,0,2):C.UVGC_781_1071,(0,0,6):C.UVGC_873_1110})

V_955 = CTVertex(name = 'V_955',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_766_1052,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_766_1054,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_766_1056,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_765_1046,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_765_1048,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_765_1050})

V_956 = CTVertex(name = 'V_956',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_564_889,(1,0,4):C.UVGC_564_890,(1,0,5):C.UVGC_564_891,(1,0,0):C.UVGC_766_1051,(1,0,8):C.UVGC_766_1052,(1,0,1):C.UVGC_766_1053,(1,0,7):C.UVGC_766_1054,(1,0,2):C.UVGC_766_1055,(1,0,6):C.UVGC_766_1056,(0,0,3):C.UVGC_563_886,(0,0,4):C.UVGC_563_887,(0,0,5):C.UVGC_563_888,(0,0,0):C.UVGC_765_1045,(0,0,8):C.UVGC_765_1046,(0,0,1):C.UVGC_765_1047,(0,0,7):C.UVGC_765_1048,(0,0,2):C.UVGC_765_1049,(0,0,6):C.UVGC_765_1050})

V_957 = CTVertex(name = 'V_957',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_279_445,(1,0,3):C.UVGC_279_446,(1,0,0):C.UVGC_747_1027,(1,0,5):C.UVGC_747_1028,(1,0,1):C.UVGC_747_1029,(1,0,4):C.UVGC_747_1030,(0,0,2):C.UVGC_279_445,(0,0,3):C.UVGC_279_446,(0,0,0):C.UVGC_747_1027,(0,0,5):C.UVGC_747_1028,(0,0,1):C.UVGC_747_1029,(0,0,4):C.UVGC_747_1030})

