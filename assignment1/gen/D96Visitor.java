// Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link D96}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface D96Visitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link D96#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(D96.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#string}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(D96.StringContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#string_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString_op(D96.String_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#bool_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_op(D96.Bool_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#relation_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelation_op(D96.Relation_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#int_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_op(D96.Int_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#float_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloat_op(D96.Float_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#int_gen_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_gen_list(D96.Int_gen_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#int_gen_cm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_gen_cm(D96.Int_gen_cmContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#bool_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_list(D96.Bool_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#bool_list_cm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_list_cm(D96.Bool_list_cmContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#float_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloat_list(D96.Float_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#float_list_cm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloat_list_cm(D96.Float_list_cmContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#string_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString_list(D96.String_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#string_list_cm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString_list_cm(D96.String_list_cmContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#lit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLit(D96.LitContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96#int_gen}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_gen(D96.Int_genContext ctx);
}