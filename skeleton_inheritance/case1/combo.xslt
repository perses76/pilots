<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
>
    <xsl:key name="blocks" match="//block" use="@name"/>

    <xsl:template match="*">            
        <xsl:variable name="blocks" select="key('blocks', name())"/>
        <xsl:element name="{ name() }">
            <xsl:choose>
                <xsl:when test="$blocks">
                    <xsl:apply-templates select="$blocks[position() = last()]" mode="block">
                    </xsl:apply-templates>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:apply-templates select="*"/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:element>
    </xsl:template>

    <xsl:template match="block">
        <!-- do nothing if it is block  -->
    </xsl:template>

    <xsl:template match="block" mode="block">
        <block name="{ @name }" source="{ @source }">
            This is block <xsl:value-of select="position()"/>
            <xsl:apply-templates select="*"/>
        </block>
    </xsl:template>

    <xsl:template match="super">
        <xsl:variable name="current_block" select="ancestor::block"/>
        <xsl:variable name="blocks" select="key('blocks', 'hello_world')"/>
        <super>
            <xsl:call-template name="apply_super">
                <xsl:with-param name="current" select="$current_block"/>
                <xsl:with-param name="items" select="$blocks"/>
            </xsl:call-template>
        </super>
    </xsl:template>


    <xsl:template name="apply_super">
        <xsl:param name="current"/>
        <xsl:param name="items"/>
        <xsl:choose>
            <xsl:when test="$items[2] = $current">
                <xsl:value-of select="$items[1]/@source"/>
                <xsl:apply-templates select="$items[1]" mode="block"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="apply_supper">
                    <xsl:with-param name="current" select="$current"/>
                    <xsl:with-param name="items" select="$items[postion() != 1]"/>
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

</xsl:stylesheet>
